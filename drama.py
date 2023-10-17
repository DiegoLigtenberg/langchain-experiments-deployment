from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os 
from PIL import Image

# You can obtain this from the Azure Portal
connection_string = "DefaultEndpointsProtocol=https;AccountName=saekmatilliontest;AccountKey=x6iqVhYaWfqH4qBwqQ4t0RqhdJb+qimxCImBqTZTdXHZ2m0aS6Q6xNysecUn0ECoUrsEqosSL2i6+AStSXfNxg==;EndpointSuffix=core.windows.net"  

container_name = "ekhome"  # Your container name
folder_name = "Images"  # Folder within the container
download_count = 10  # Number of images to download

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Create a ContainerClient for the specified container
container_client = blob_service_client.get_container_client(container_name)

# Specify the local directory where you want to save the downloaded files
local_directory = r"F:\GitHub\langchain-experiments-deployment\Images"  # Replace with your desired local directory

# Ensure the local directory exists; create it if it doesn't
os.makedirs(local_directory, exist_ok=True)

# List all blobs in the specified folder
blobs_in_folder = container_client.walk_blobs(folder_name)
downloaded_count = 0

for blob in blobs_in_folder:
    if downloaded_count >= download_count:
        break  # Stop downloading once you reach the desired count

    blob_name = blob.name
    # local_filename = os.path.join(local_directory, blob_name)
    local_filename = blob_name

    # Download the blob to a local file
    blob_client = container_client.get_blob_client(blob_name)
    with open(r'C:\ek-images\Images2', "wb") as f:
            data = blob_client.download_blob()
            data.readinto(f)
    # asd

    # Process the downloaded image here

    downloaded_count += 1
    print(blob.name)
    print(len(blobs_in_folder))
    asd
