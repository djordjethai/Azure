import json
import streamlit as st
from mojafunkcja import st_style
from azure.storage.blob import BlobServiceClient, BlobClient
import pandas as pd
from streamlit_javascript import st_javascript


st_style()

rights = ""
# Function to fetch AAD username using JavaScript
filename = "data.json"
container_name = "positive-user"
constr = "DefaultEndpointsProtocol=https;AccountName=positiveuserinfo;AccountKey=jGsj6JqKj+R5lEPG5VWX3YLo5sZswBt2Gij/KatcKkbYudB/mcrSeQzjf3NNyf8gUfgYrDkMHK8J+AStHs0mlA==;EndpointSuffix=core.windows.net"  # your connection string


def load_data():
    try:
        blob_service_client = BlobServiceClient.from_connection_string(constr)
        container_client = blob_service_client.get_container_client(
            container_name)
        blob_client = container_client.get_blob_client(filename)

        streamdownloader = blob_client.download_blob()
        data = json.loads(streamdownloader.readall())
        return data
    except FileNotFoundError:
        return {"user_list": []}


def read_aad_username():
    js_code = """(await fetch("/.auth/me")
        .then(function(response) {return response.json();}).then(function(body) {return body;}))
    """

    return_value = st_javascript(js_code)

    username = None
    if return_value == 0:
        pass  # this is the result before the actual value is returned
    elif isinstance(return_value, list) and len(return_value) > 0:  # this is the actual value
        username = return_value[0]["user_id"]
        st.write(f"Logged in as {username}")
    else:
        st.warning(
            f"could not directly read username from azure active directory: {return_value}.")  # this is an error
        st.warning(
            f"A workaround to this is to clear your browser cookies for this site and reloading it.")
    return username


# Get the current user's username
current_user = read_aad_username()
phtable = st.empty()
st.info(
    f"Current User is: {current_user} ")


# Read data from JSON file

filename = "data.json"
container_name = "positive-user"
constr = "DefaultEndpointsProtocol=https;AccountName=positiveuserinfo;AccountKey=jGsj6JqKj+R5lEPG5VWX3YLo5sZswBt2Gij/KatcKkbYudB/mcrSeQzjf3NNyf8gUfgYrDkMHK8J+AStHs0mlA==;EndpointSuffix=core.windows.net"  # your connection string
data = load_data()


with phtable.container():
    st.subheader("User list: ")
    df = pd.DataFrame(data['user_list'])
    st.table(df)


# Access the user list from the JSON dictionary
user_list = data['user_list']
nasao = False

# current_user = "djordje@positive.rs" # for testing purposes

for user in user_list:
    if user["name"] == current_user:
        rights = user["rights"]
        # Action if the user is found in the list
        st.success(
            f"User found in the list and has {rights} rights to use this part of the application")
        # You can call a function here to perform some action
        nasao = True

if not nasao:
    st.warning("User not found in the list")
    # The user is not authorized to use this part of the application

# # The data.json file can contain additional elements such as access rights, etc.
# # Additionally, you can store data.json in an Azure Blob to avoid redeployment on data changes.