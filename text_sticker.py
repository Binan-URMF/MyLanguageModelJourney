import os

def concatenate_files(directory_path, output_file):
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as infile:
                    outfile.write(infile.read())

concatenate_files('inaugural', 'us_pres.txt')