# TXT Duplicate File Finder

A Python script that recursively searches through a directory and its subdirectories to find duplicate `.txt` files based on their content.

## Features

- **Recursive Search:** Searches through the specified directory and all its subdirectories.
- **File Size Comparison:** Groups text files by size to reduce unnecessary hash calculations.
- **SHA-256 Hashing:** Uses the SHA-256 algorithm to compare file contents.
- **Duplicate Detection:** Identifies files with identical content, even if they have different filenames or locations.
- **Permission Error Handling:** Handles access-denied errors and continues processing accessible files.
- **File Path Reporting:** Prints the paths of detected duplicate files.

## How It Works

The program follows these steps:

1. Takes a directory path as input.
2. Lists the files and directories inside the specified path.
3. Recursively searches through subdirectories.
4. Identifies `.txt` files and groups them by file size.
5. Calculates the SHA-256 hash of each file in the same size group.
6. Groups files with identical hashes and reports groups containing more than one file.
7. Prints the paths of the detected duplicate files.

## Requirements

- Python 3.x
- Standard Python libraries:
  - `os`
  - `hashlib`

No external packages are required.

## How to Run

1. Make sure Python is installed on your system.
2. Save the script as `duplicate_finder.py`.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python duplicate_finder.py
```

5. Enter the path of the directory you want to scan when prompted.

### Example

**Input:**

```text
Enter folder path: C:\Users\User\Documents
```

**Output:**

```text
Duplicate files:
C:\Users\User\Documents\file1.txt
C:\Users\User\Documents\backup\file1_copy.txt
```

*Note: The output is an illustrative example. Actual results depend on the files in the selected directory.*

## Limitations

- Only files ending in `.txt` are processed.
- File extensions are case-sensitive, so `.TXT` files are not included.
- Files with different sizes are not compared, since identical content normally produces files of the same size.
- The program reports duplicate files but does not delete or modify them.
- Other operating system errors, such as certain file-not-found errors, are not explicitly handled.

## Concepts Practiced

This project demonstrates practical use of:

- File and directory management with `os`
- Recursive functions
- Exception handling with `try` and `except`
- File size inspection
- Binary file reading
- Cryptographic hashing with SHA-256
- Dictionaries and lists for grouping data
- Algorithmic optimization through preliminary filtering

## Future Improvements

- Support additional file extensions.
- Make file extension matching case-insensitive.
- Improve error handling for inaccessible or changing files.
- Add a summary showing the number of duplicate groups and files found.
- Optimize memory usage when hashing large files.

---

**Project Type:** Python Learning Project  
**Category:** File System Automation  
**Status:** Initial Version