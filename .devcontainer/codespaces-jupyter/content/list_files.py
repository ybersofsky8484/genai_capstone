import os

folder_path = "./"

# Get only PDF files
pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

# Save to a text file
output_file = "files_list.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for file in pdf_files:
        f.write(file + "\n")

print(f"Saved {len(pdf_files)} file names to {output_file}")
