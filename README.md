# README
This scripts converts a DayOne v1 Diary from this .doentry (plist) to an more readable markdown and then to LaTeX. It creates a book.

## How to Use
1. setup folders / adjust folder paths
1. run `python convert_dayone2md.py`
2. run `python create_journal_latex.py`

# Ideas
## DayOne File Structure
How to find Images-> Images are in the "photos" directory and have the identical UUID as the text files.
First Line is mostly none heading. Need to added a markdown heading.

## Convert information
When converting Markdown to LaTeX -> add --warp=none to not wrap text in Source code.

## Ideas for Problems
Numbered sections -> iterate through each file when processing with python and replace \section{} with \section*{}
