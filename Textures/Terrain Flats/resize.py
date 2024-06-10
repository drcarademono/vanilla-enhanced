import os
import subprocess
import pandas as pd

# Load the CSV file
csv_file_path = 'NatureFlatsMeshDimensions.csv'
mesh_dimensions_df = pd.read_csv(csv_file_path)

# Directory containing the images
image_directory = '.'

# Iterate over each row in the CSV
for index, row in mesh_dimensions_df.iterrows():
    archive = row['Archive']
    record = row['Record']
    scale = row['Scale']
    
    # Construct the filename
    filename = f"{int(archive)}_{int(record)}-0.png"
    filepath = os.path.join(image_directory, filename)
    
    # Check if the file exists
    if os.path.isfile(filepath):
        # Construct the ImageMagick command
        resize_percentage = scale * 100
        command = f"convert {filepath} -interpolate integer -filter point -resize {resize_percentage}% {filepath}"
        
        # Execute the command
        subprocess.run(command, shell=True)
    else:
        print(f"File {filename} does not exist and will be skipped.")

