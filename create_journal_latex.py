#!/usr/bin/env python

import os
import sys
import re
from os import listdir
from datetime import datetime
import locale
import argparse

# Set arguments
parser = argparse.ArgumentParser(description="Converts Markdown files to one LaTeX file. For DayOne dairy conversion.")
parser.add_argument("-y", "--year", help="Only output entries of a specific year.", type=int, dest='year')
parser.add_argument("-a", "--author", help="Add the Authors name.", type=str, dest='author')
parser.add_argument("-i", "--input", help="Input directory", type=str, dest='input_dir')
args = parser.parse_args()

# Set directories
dir = 'small-library'
if args.input_dir:
    dir = args.input_dir
latex_template = 'Journal_template.tex'
latex_output = 'Journal_output.tex'
output_file_folder = 'output/'
output_dir = 'latex_output/'
locale.setlocale(locale.LC_ALL, "de_DE")

# Returns the date saved in filename
def get_date_of_filename(filename_date):
    filename_date = filename_date.split('.')[0]
    if '+' in filename_date:
        date = datetime.strptime(filename_date.split('+')[0], "%Y-%m-%d %H:%M:%S")
    else:
        date = datetime.strptime(filename_date, "%Y-%m-%d %H:%M:%S")
    return date

def process_file(file):
    filename = file.split('.')[0]
    # Convert from markdown to LaTeX with pandoc
    if not os.path.exists(dir + '/' + output_dir):
        os.makedirs(dir + '/' + output_dir)
    if not os.path.exists(dir + '/' + '/markdown_output/'):
        os.makedirs(dir + '/' + '/markdown_output/')
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

# If year is set per argument -> print this info
if args.year:
    print "Year " + str(args.year) + " will be processed.\n"

# Create output folder if it not exists
if not os.path.exists(dir + '/' + output_dir):
    os.makedirs(dir + '/' + output_dir)
if not os.path.exists(output_file_folder):
    os.makedirs(output_file_folder)

# Write content directly in LaTeX output
document = open(output_file_folder + 'Journal_output.tex', 'w')
try:
    template = open(latex_template, 'r')
except IOError:
    print("Couldn't find Journal template. Exiting.")
    sys.exit()
print('Read journal template.')

files_entries = listdir(dir + '/markdown_output')
# sort list by datetime
files_entries.sort()

for file in files_entries:
    if not file.endswith('.md'):
        files_entries.remove(file)

template_tex = template.read()

# Add author at title page
if args.author:
    template_tex = re.sub(r"\\author{\w*}", r"\\author{" + args.author + "}", template_tex)

# Add correct date at title page
if args.year:
    template_tex = re.sub(r"\\date{\w*}", r"\\date{" + str(args.year) + "}", template_tex)
else:
    template_tex = re.sub(r"\\date{\w*}", r"\\date{" + get_date_of_filename(files_entries[0]).strftime("%d.%m.%Y") + " - " + get_date_of_filename(files_entries[-1]).strftime("%d.%m.%Y") + "}", template_tex)

document.write(template_tex + '\n')

# Iterate each file in folder
for file in files_entries:
    if not args.year:
        process_file(file)
    # Process only files which year is the one in argument
    else:
        creation_date = get_date_of_filename(file)
        if args.year == creation_date.year:
            process_file(file)
        else:
            continue

document.write('\n\\end{document}')
print('writed journal_output.tex\nFinished.')
