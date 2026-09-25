import os
import shutil

# Source folder containing JPG files
source_folder = "test_files"

# Destination folder
destination_folder = "jpg_files"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Count moved files
moved_files = 0

# Check all files in the source folder
for file in os.listdir(source_folder):

    # Check if the file is a JPG file
    if file.lower().endswith((".jpg","jpeg")):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        # Move the JPG file
        shutil.move(source_path, destination_path)

        print(f"Moved: {file}")
        moved_files += 1

print("\nFile organization completed!")
print(f"Total JPG files moved: {moved_files}")