# Recursive TXT Word Search

A Python program that recursively searches through folders
and finds .txt files containing a specific word.

## Features

- Searches through folders recursively
- Searches only .txt files
- Finds the requested word inside each file
- Returns the names of matching files

## Concepts Learned

- Functions
- Recursion
- Lists
- File Handling
- `os` module
- `try/except`
- `break`
- `return`

## How It Works

1. The user enters a folder path.
2. The user enters a word to search for.
3. The program searches through the folder and its subfolders.
4. It opens `.txt` files and checks their lines.
5. If the word is found, the file name is added to the results.

## Example

Input:

Folder path:
D:\Documents

Word:
Python

Output:

['book.txt', 'notes.txt']