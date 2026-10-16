# File Organizer

A Python program that organizes files in a folder based on their file extensions.

## Features

* Scans files and directories recursively.
* Detects file extensions using `os.path.splitext()`.
* Creates folders based on file extensions.
* Moves files into their corresponding folders.
* Skips files without extensions.
* Handles `PermissionError`.

## Example

Before:

```text
Downloads/
├── photo.jpg
├── document.txt
├── music.mp3
└── image.png
```

After:

```text
Downloads/
├── jpg/
│   └── photo.jpg
├── txt/
│   └── document.txt
├── mp3/
│   └── music.mp3
└── png/
    └── image.png
```

## Concepts Practiced

* `os.listdir()`
* `os.path.join()`
* `os.path.isdir()`
* `os.path.splitext()`
* `os.path.exists()`
* `os.mkdir()`
* `shutil.move()`
* `try/except`
* `continue`
* Recursion
