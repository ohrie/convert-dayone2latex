# Need to have: LaTeX Template, pandoc

import os
import re
from os import listdir
from datetime import datetime
import locale
import argparse

dir = 'small-library'
latex_template = 'Journal_template.tex'
latex_output = 'Journal_output.tex'
output_dir = 'latex_output/'
locale.setlocale(locale.LC_ALL, "de_DE")

def process_file(file):
    filename = file.split('.')[0]

    # Convert from markdown to LaTeX with pandoc
    os.system("pandoc --wrap=none -o \"" + dir + '/' + output_dir + filename + '.tex\"  \"' + dir + '/markdown_output/' + filename + '.md\"' )
    current_entry = open(dir + '/' + output_dir + filename + '.tex' , 'r')
    current_entry_text = current_entry.read()

    if '+' in filename:
        creation_date = datetime.strptime(filename.split('+')[0], "%Y-%m-%d %H:%M:%S")
        entry_location = filename.split('+')[1]
        current_entry_text = re.sub(r"(\\section{.*})", r"\1\n\\textbf{" + creation_date.strftime("%w. %B %Y, %H:%M") + r"} \\textit{" + entry_location + r"}\\\\", current_entry_text)
    else:
        creation_date = datetime.strptime(filename, "%Y-%m-%d %H:%M:%S")
        current_entry_text = re.sub(r"(\\section{.*})", r"\1 \n\\textbf{" + creation_date.strftime("%w. %B %Y, %H:%M") + r"}", current_entry_text)


    # Replace numbered with unnumbered sections
    current_entry_text = current_entry_text.replace('\section', '\section*')
    current_entry_text = current_entry_text.replace('\subsection', '\subsection*')
    current_entry_text = current_entry_text.replace('\subsubsection', '\subsubsection*')
    document.write(current_entry_text + '\n%-------------------next-entry-------------------\n')
    print(file + ' converted to latex\n')

# Set arguments
parser = argparse.ArgumentParser(description="Converts Markdown files to one LaTeX file. For DayOne dairy conversion.")
parser.add_argument("-y", "--year", help="Only output entries of a specific year.", type=int, dest='year')
args = parser.parse_args()
if args.year:
    print "Year " + str(args.year) + " will be processed.\n"

# Create output folder if it not exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Write content directly in LaTeX output
document = open('Journal_output.tex', 'w')
try:
    template = open(latex_template, 'r')
except IOError:
    print("Couldn't find Journal template. Exiting.")
    sys.exit()
print('read journal template')
files_entries = listdir(dir + '/markdown_output')
document.write(template.read() + '\n')

# sort list by datetime
files_entries.sort()

for file in files_entries:
    if file.endswith('.md'):
        process_file(file)

document.write('\n\\end{document}')
print('writed journal_output.tex\nFinished.')
