import os

# Path to the folder containing the PNG files
folder_path = '.'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.png'):
        # Split the filename to get the first part before the underscore
        parts = filename.split('_')
        if len(parts) > 1:
            # Increment the first prefix by 1
            prefix = int(parts[0]) + 1
            # Rebuild the filename with the incremented prefix
            new_filename = f'{prefix}_{parts[1]}'
            # Get the full file paths
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {filename} -> {new_filename}')

