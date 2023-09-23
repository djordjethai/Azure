# Azure Blob Access Control Streamlit App

## Overview

This repository contains Python code for a Streamlit web application that provides access control to certain parts of the application based on user information stored in a JSON file hosted on Azure Blob Storage. This app allows users to log in and checks their access rights against the data in the JSON file. If the user has the required rights, they can use the protected part of the application.

## Prerequisites

App only runs correctly if you are running it form an Azure App Service with enabled authentication, or have aquired a token from Azure AD in another way.

Before running the application, make sure you have the following prerequisites set up:

1. Azure Blob Storage Account: You should have an Azure Blob Storage account where you will host the `data.json` file containing user information.

2. Azure Blob API Key: You will need the Azure Blob Storage API key to access the `data.json` file.

3. Streamlit: You should have Streamlit installed on your local machine.

## Installation and Usage

Follow these steps to install and run the application:

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd azure-blob-access-control-app
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set the environment variables:

   - `AZ_BLOB_API_KEY`: Set this variable to your Azure Blob API key.

5. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

6. Access the application in your web browser at the provided URL.

## Usage

1. When you access the application, it will use JavaScript to fetch the currently logged-in Azure Active Directory (AAD) user's username.

2. It will then check if the username is found in the `data.json` file hosted on Azure Blob Storage. If the user is found and has the required rights, they will be granted access to the protected part of the application.

3. If the user is not found or does not have the required rights, a warning message will be displayed, indicating that the user does not have access.

## Customization

You can customize this application by modifying the following parts:

- `data.json`: This JSON file should contain user information, including usernames and access rights. You can add or remove users as needed.

- Access Control Logic: You can modify the logic for access control and define what actions should be taken when a user is authorized or not authorized.

## Additional Notes

- You can enhance security by using Azure Blob Storage's built-in access control features to restrict access to the `data.json` file.

- The application provides flexibility in controlling user access to different parts of your application, making it suitable for various use cases.

Feel free to use this code as a starting point for building access-controlled web applications with Streamlit and Azure Blob Storage.
