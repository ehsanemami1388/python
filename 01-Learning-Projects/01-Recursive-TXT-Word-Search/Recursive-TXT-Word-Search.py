
import os


def search(folder_path, search_word):
    # List of files and folders found in the current directory
    results = []

    try:
        for file_name in os.listdir(folder_path):

            current_path = os.path.join(folder_path, file_name)

            # If the current path is a folder, search inside it recursively
            if os.path.isdir(current_path):
                results += search(current_path, search_word)

            # Search only inside .txt files
            if file_name.endswith(".txt"):

                with open(
                    current_path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as file:

                    # Check every line of the file
                    for line in file:

                        # If the searched word is found, save the file name
                        if search_word in line:
                            results.append(file_name)

                            # Stop checking this file after finding the word
                            break

    except PermissionError:
        print("Access denied:", folder_path)

    return results


folder_path = input("Write folder path: ")
search_word = input("Write a word to search: ")

print(search(folder_path, search_word))
