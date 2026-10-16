
import os
import shutil


def file_organizer(path):
    for file_name in os.listdir(path):

        current_path = os.path.join(path, file_name)

        # If the current item is a directory, search it recursively.
        if os.path.isdir(current_path):
            file_organizer(current_path)
            continue

        # Separate the file name and extension.
        name, extension = os.path.splitext(current_path)

        # Skip files without an extension.
        if extension == "":
            continue

        # Remove the dot from the extension.
        folder_name = extension.lstrip(".")

        # Create the destination path.
        destination = os.path.join(path, folder_name)

        try:
            # If the destination folder already exists, move the file.
            if os.path.exists(destination):
                shutil.move(current_path, destination)

            # Otherwise, create the folder and then move the file.
            else:
                os.mkdir(destination)
                shutil.move(current_path, destination)

        except PermissionError:
            print("Access denied:", current_path)


path = input("Enter folder path: ")
file_organizer(path)

