import os
import zipfile
import gzip
import shutil
import random
from pathlib import Path

# Paths
downloads_folder = str(Path.home() / "Downloads")  # Default Downloads folder
destination_folder = str(Path.home() / "Documents" / "extracted_pys")  # Destination for extracted files

# Step 1: Find the latest .zip file
def find_latest_zip(folder):
    zip_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".zip")]
    if not zip_files:
        print("No .zip files found in the Downloads folder.")
        return None
    latest_zip = max(zip_files, key=os.path.getmtime)
    return latest_zip

# Step 2: Extract the .zip file
def extract_zip(zip_path, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)
    print(f"Extracted {zip_path} to {dest_folder}")

# Step 3: Extract .gzip and .gz files
def extract_gz_files(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith((".gz", ".gzip")):
                gzip_path = os.path.join(root, file)
                extracted_path = os.path.join(root, os.path.splitext(file)[0])  # Remove .gz/.gzip extension
                if "XMLPAIN" in extracted_path:
                    extracted_path = extracted_path + ".xml"
                try:
                    with gzip.open(gzip_path, 'rb') as f_in:
                        with open(extracted_path, 'wb') as f_out:
                            shutil.copyfileobj(f_in, f_out)
                    os.remove(gzip_path)  # Optional: Remove the original .gz/.gzip file
                    print(f"Extracted {gzip_path} to {extracted_path}")
                except Exception as e:
                    print(f"Failed to extract {gzip_path}: {e}")

def oldify_files(destination_folder):
    # Create the 'old' subfolder if it doesn't exist
    old_folder = os.path.join(destination_folder, "old")
    if not os.path.exists(old_folder):
        os.makedirs(old_folder)
        print("Old folder created...\n")

    # List all files in the directory
    files_in_dir = os.listdir(destination_folder)
    for f in files_in_dir:
        file_path = os.path.join(destination_folder, f)  # Full path of the file or folder

        # Skip the 'old' folder itself
        if f == "old":
            continue

        if os.path.isdir(file_path):  # Ensure it's a file
            # Resolve naming conflicts
            new_file_name = f
            while new_file_name in os.listdir(old_folder):
                # Generate a new name with a random suffix
                name, ext = os.path.splitext(f)
                new_file_name = f"{name}_{random.randint(1000, 9999)}{ext}"

            # Move the file to the 'old' folder with the resolved name
            new_file_path = os.path.join(old_folder, new_file_name)
            shutil.move(file_path, new_file_path)
            print(f"[!OLDIFIED!] Moved {f} to {new_file_path}")

def main():
    print("Starting extraction process...")
    oldify_files(destination_folder)
    latest_zip = find_latest_zip(downloads_folder)
    if latest_zip:
        print(f"Latest ZIP file: {latest_zip}")
        latest_zip_name = os.path.basename(latest_zip)
        extract_zip(latest_zip, (destination_folder + r"\extracted_" + (latest_zip_name.split(".zip")[0])))
        print("Unzipping complete. Now extracting .gzip and .gz files...")
        extract_gz_files(destination_folder)
    else:
        print("No ZIP file to process.")

if __name__ == "__main__":
    main()