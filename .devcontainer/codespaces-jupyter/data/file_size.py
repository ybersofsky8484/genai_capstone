import os

zip_path = "/codespaces-jupyter/data/papers.zip"
size_bytes = os.path.getsize(zip_path)
size_mb = size_bytes / (1024 * 1024)
print(f"ZIP file size: {size_mb:.2f} MB")