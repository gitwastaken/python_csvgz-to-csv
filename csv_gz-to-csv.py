# List files in a directory and check if the files are *.csv.gz then extracts all to *.csv
# import Module
import os
import gzip
import shutil
import ntpath

# Define Path
path = "C:\\Users\Bhavneet Singh\Downloads\\testinggz"

# Change dur to new location using path
os.chdir(path)
# cwd = os.getcwd()
# print(cwd)

# Read the file
def read_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())


# iterate through all files
for file in os.listdir():
    # checking if the file/s is in which specified format
    if file.endswith(".csv.gz"):
        file_path = f"{path}\{file}"
        #print(file_path)
        file_name = ntpath.basename(file_path)
        print(f"File you want to extract: {file_name}")
        exact_file_name = (os.path.splitext(file_name)[0])
        print(f"File you will be getting after extract: {exact_file_name}")
        """
        # calling function to read the file/s
        # read_file(file_path)
        # decompressing the file in same location
        """
        with gzip.open(file_name, 'rb') as f_in:
            with open(exact_file_name, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

