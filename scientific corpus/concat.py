import os

# Directory path
directory = '/Users/ezelbayraktar/Documents/DL-NLP/MyLanguageModelJourney/scientific corpus/'

# Output file name
output_file = 'sci_corp.txt'

# List all text files in the directory
text_files = [file for file in os.listdir(directory) if file.endswith('.txt')]

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Iterate over each text file
    for file in text_files:
        # Open each text file in read mode
        with open(os.path.join(directory, file), 'r') as infile:
            # Read the contents of the file
            contents = infile.read()
            # Write the contents to the output file
            outfile.write(contents)

print('Total words in the corpus: ', len(open(output_file).read().split()))