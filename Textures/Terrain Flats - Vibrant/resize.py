import os
import subprocess

# Replace 'your_folder_path' with the actual path to your folder containing the PNG files
folder_path = os.getcwd()
png_files = [f for f in os.listdir(folder_path) if f.endswith('.png') and not f.endswith('-size.png')]

for file in png_files:
    base_name = file.rsplit('.', 1)[0]
    size_variant = f"{base_name}-size.png"
    if size_variant in os.listdir(folder_path):
        original_file_path = os.path.join(folder_path, file)
        size_file_path = os.path.join(folder_path, size_variant)
        
        # Get dimensions of the -size image
        size_output = subprocess.run(['identify', '-format', '%wx%h', size_file_path], capture_output=True, text=True)
        if size_output.returncode == 0:
            size_dimensions = size_output.stdout.strip()
            
            # Resize original file to match -size dimensions, ensuring the point filter is used
            resize_command = [
                'convert', original_file_path,
                '-filter', 'point',
                '-resize', size_dimensions,
                '-interpolate', 'integer',
                original_file_path  # Overwrite the original file, or specify a new output path if you prefer
            ]
            subprocess.run(resize_command)
        else:
            print(f"Failed to get dimensions for {size_variant}")
    else:
        print(f"No corresponding -size variant found for {file}")

