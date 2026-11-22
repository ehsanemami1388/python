import os
from pathlib import Path
def Find_and_Analyze_Text_Files(path_folder):
    chek_txt =0
    data={}
    most_words_file={"most_words_file":None,
                    "name_of":[]
                    }
    for paths in os.listdir(path_folder):

        newpath=os.path.join(path_folder,paths)
        if os.path.isdir(newpath):
            continue
        chek = Path(newpath)

        if chek.suffix.lower() == ".txt":


            try:
                with open(
                    newpath,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                    )as file:
                    data[paths] = {
                                "total_lines": 0,
                                "total_words": 0,
                                "total_characters": 0,
                                "total_pythons": 0
                                }
                    chek_txt+=1
                    for line in file:
                        data[paths]["total_lines"]+=1
                        words=line.split()
                        data[paths]["total_words"] += len(words)
                        data[paths]["total_characters"] += len(line)
                        for word in words:
                            if word.lower()== "python":
                                data[paths]["total_pythons"]+=1
                    if most_words_file["most_words_file"] == None:
                        most_words_file["most_words_file"] = data[paths]["total_words"]
                        most_words_file["name_of"].append(paths)
                    elif most_words_file["most_words_file"] < data[paths]["total_words"]:
                        most_words_file["most_words_file"] = data[paths]["total_words"]
                        most_words_file["name_of"].clear()
                        most_words_file["name_of"].append(paths)
                    elif most_words_file["most_words_file"] == data[paths]["total_words"]:
                        most_words_file["name_of"].append(paths)


            except PermissionError as e:
                print("error",e)
    if chek_txt ==0:
        print("you dont have any txt file")
    return data , most_words_file

path_folder = input("Enter your folder path: ")
result = Find_and_Analyze_Text_Files(path_folder)

print("File analysis:")
for file_name, file_data in result[0].items():
    print(file_name, file_data)

print("File(s) with the most words:")
print(result[1])