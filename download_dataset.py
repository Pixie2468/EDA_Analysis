import kagglehub
import os
import shutil

# Define the dataset identifier and the destination directory
dataset_id = "aiaiaidavid/the-big-dataset-of-ultra-marathon-running"
destination_dir = "data"

# Download the dataset to a temporary cache location
downloaded_path = kagglehub.dataset_download(dataset_id)

# Create the data directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Move the downloaded files from the cache to the data directory
# The downloaded_path is a directory containing the unzipped files
for filename in os.listdir(downloaded_path):
    source = os.path.join(downloaded_path, filename)
    dest = os.path.join(destination_dir, filename)
    shutil.move(source, dest)

print(f"Dataset downloaded to: {destination_dir}")
