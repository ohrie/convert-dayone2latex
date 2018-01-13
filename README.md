# README
This scripts converts a DayOne v1 Diary from this .doentry (plist) to a pdf.
First it creates more readable Markdown files, then LaTeX. Then a pdf of the specified files will be created. It creates a book.

## How to Use
1. setup folders / adjust folder paths
1. run `python convert_dayone2md.py`
2. run `python create_journal_latex.py`

# Ideas
## DayOne File Structure
How to find Images-> Images are in the "photos" directory and have the identical UUID as the text files.
First Line is mostly none heading. Need to added a markdown heading.
