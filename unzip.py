# Tool to automate extracting from zip folders in the Arrivals area to a single specified destination f
# Note: this takes a lot longer than manually doing it, but automation allows you to leave it runing and
import os
import zipfile

# Path to the directory containing the zip files
zip_folder = "Q:/uceesro/24-0003899-part2_Extract/DrugIssue"

# Path to the destination folder where the extracted files will be saved
destination_folder = "S:/CDSTP_CPRD_24_003899/Aurum_Extract/Aurum_Data_Extract_Part_2/DrugIssue"

# Get a list of all the zip files in the zip folder
zip_files = [file_name for file_name in os.listdir(zip_folder) if file_name.endswith('.zip')]

# Iterate over each file in the zip folder
for file_name in zip_files:
    # Construct the full path to the current file
    file_path = os.path.join(zip_folder, file_name)
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        # Extract all files in the zip to the destination folder
        zip_ref.extractall(destination_folder)

# Alternatively, test:
# Imports
#from zipfile import ZipFile
#from glob import glob
