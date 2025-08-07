import zipfile
import os

def zip_folder(folder_path, output_path):
    # Create a ZipFile object in write mode
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through all files in the folder
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Add file to the zip, preserving folder structure
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
    print("Zipping complete!")  # Confirmation message


# Usage
zip_folder("/codespaces-jupyter/notebooks/data", "papers.zip")
