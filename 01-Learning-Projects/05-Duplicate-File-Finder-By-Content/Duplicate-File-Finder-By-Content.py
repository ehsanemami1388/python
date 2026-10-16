
import os
import hashlib


def find_duplicates(path):
    groups = {}
    duplicates = []

    # Search through all files and directories
    try:
        path_files = os.listdir(path)
    except PermissionError:
        print("Access denied:", path)
        return duplicates

    for path_file in path_files:
        new_path = os.path.join(path, path_file)

        # Search inside subdirectories recursively
        if os.path.isdir(new_path):
            duplicates += find_duplicates(new_path)
            continue

        # Only process TXT files
        if new_path.endswith(".txt"):
            try:
                current_size = os.path.getsize(new_path)

                # Group files by their size
                if current_size not in groups:
                    groups[current_size] = [new_path]
                else:
                    groups[current_size].append(new_path)

            except PermissionError:
                print("Access denied:", new_path)

    # Check files with the same size
    for size, files in groups.items():
        hash_files = {}

        # Calculate a hash for each file
        for file_path in files:
            try:
                with open(file_path, "rb") as f:
                    new_hash = hashlib.sha256(f.read()).hexdigest()

                # Group files by their hash
                if new_hash not in hash_files:
                    hash_files[new_hash] = [file_path]
                else:
                    hash_files[new_hash].append(file_path)

            except PermissionError:
                print("Access denied:", file_path)

        # Find duplicate files
        for files in hash_files.values():
            if len(files) > 1:
                duplicates.extend(files)

    return duplicates


path = input("Enter folder path: ")
duplicates = find_duplicates(path)

print("\nDuplicate files:")
for file_path in duplicates:
    print(file_path)
