# Need to have: LaTeX Template, pandoc

import os
from os import listdir

dir = 'small-library'
latex_template = 'Journal_template.tex'
latex_output = 'Journal_output.tex'

def process_file(file):
    filename = file.split('.')[0]
    # Convert from markdown to LaTeX with pandoc
    os.system("pandoc -o " + dir + '/latex_output/' + filename + '.tex ' + dir + '/markdown_output/' + file )
    current_entry = open(dir + '/latex_output/' + filename + '.tex' , 'r')
    # Replace numbered with unnumbered sections
    current_entry_text = current_entry.read()
    current_entry_text = current_entry_text.replace('\section', '\section*')
    current_entry_text = current_entry_text.replace('\subsection', '\subsection*')
    current_entry_text = current_entry_text.replace('\subsubsection', '\subsubsection*')
    document.write(current_entry_text + '\n')
    print(file + ' converted to latex\n')

# Write content directly in LaTeX output
document = open('Journal_output.tex', 'w')
try:
    template = open(, 'r')
except IOError:
    print("Couldn't find Journal template. Exiting.")
    sys.exit()
print('read journal template')
files_entries = listdir(dir + '/markdown_output')
document.write(template.read() + '\n')

for file in files_entries:
    process_file(file)

document.write('\n\\end{document}')
print('writed journal_output.tex\nFinished.')
