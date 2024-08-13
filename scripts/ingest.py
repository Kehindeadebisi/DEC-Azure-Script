import os
from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient, FileSystemClient

storage_account_name = "kowopesta"
local_path = "/Users/mac/AZDEC/scripts" 
file_name = "kowope-daily-reports.csv"

def get_service_client(account_name: str) -> DataLakeServiceClient:
    try:
        credential = DefaultAzureCredential()
        service_client = DataLakeServiceClient(
            account_url=f"https://{account_name}.dfs.core.windows.net",
            credential=credential
        )
        return service_client
    except Exception as e:
        print(f"Failed to create service client: {e}")
        return None

service_client = get_service_client(storage_account_name)

def get_or_create_file_system(service_client: DataLakeServiceClient, file_system_name: str) -> FileSystemClient:
    try:
        file_system_client = service_client.get_file_system_client(file_system_name)
        if not file_system_client.exists():
            file_system_client.create_file_system()
            print(f"File system '{file_system_name}' created successfully.")
        else:
            print(f"File system '{file_system_name}' already exists.")
        return file_system_client
    except Exception as e:
        print(f"Error accessing file system: {e}")
        return None

file_system_client = get_or_create_file_system(service_client, "kowopecon")

def create_directory(file_system_client: FileSystemClient, directory_name: str):
    try:
        directory_client = file_system_client.get_directory_client(directory_name)
        if not directory_client.exists():
            directory_client.create_directory()
            print(f"Directory '{directory_name}' created successfully.")
        else:
            print(f"Directory '{directory_name}' already exists.")
        return directory_client
    except Exception as e:
        print(f"Error creating directory: {e}")
        return None

directory_client = create_directory(file_system_client, "kowopefile")

def upload_to_directory(directory_client, local_path: str, file_name: str):
    try:
        file_client = directory_client.get_file_client(file_name)
        file_client.create_file()
        
        with open(os.path.join(local_path, file_name), mode="rb") as data:
            file_client.upload_data(data, overwrite=True)
            print(f"File '{file_name}' uploaded successfully.")
    except Exception as e:
        print(f"Error uploading file: {e}")

if directory_client is not None:
    upload_to_directory(directory_client, local_path, file_name)
else:
    print("Failed to create directory client, skipping file upload.")
