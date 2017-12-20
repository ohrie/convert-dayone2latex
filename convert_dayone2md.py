import plistlib
import os
from os import listdir

# Set directories
input_dir = "small-library"
output_dir = "small-library/markdown_output"
files_entries = listdir(input_dir + '/entries')
files_photos = listdir(input_dir + '/photos')
files_dayone = []

def convert_file(file):
    # Get files
    current_filename = file.split('.')[0]
    print(current_filename + ' started processing')
    files_dayone.append(current_filename)
    current_file = open(output_dir + '/' + current_filename + '.md', 'w')
    journal_entry = plistlib.readPlist( input_dir + '/entries/'+ current_filename +'.doentry')
    print(current_filename + " read")
    # Get journal text
    journal_entry_text = journal_entry['Entry Text'].encode('utf-8')
    # Add markdown heading
    journal_lines = journal_entry_text.splitlines()
    journal_lines[0] = '# ' + journal_lines[0]

    # Add image url
    for photo in files_photos:
        if photo.startswith(current_filename):
            journal_lines.insert(1, '\includegraphics[width=\\textwidth]{' + input_dir + '/photos/' + current_filename + '.jpg}')

    journal_entry_text = '\n'.join(journal_lines)
    print(current_filename + " processed")
    # Write markdown file
    current_file.write(journal_entry_text)
    print(current_filename + " saved")
    return

print('found ' + str(len(files_entries)) + ' files in ' + input_dir + '/entries')
print('found ' + str(len(files_photos)) + ' files (photos) in ' + input_dir + '/photos')
number_files = 0
for file in files_entries:
    if file.endswith('.doentry'):
        convert_file(file)
        print('----------------------------')
        number_files += 1

print('processed ' + str(number_files) + ' files')
print('finished')
