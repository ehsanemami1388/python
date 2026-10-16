import os 
def search(path ):
    stats = {
        "file_count": 0,
        "total_lines": 0,
        "total_characters": 0,
        "largest_size": 0,
        "largest_file": ""
    }
    try :
        for path_name in os.listdir(path):
            current_path = os.path.join(path,path_name)
            if os.path.isdir(current_path):
                file_stats = search(current_path) 
                if stats ["largest_size"] < file_stats ["largest_size"] :
                    stats ["largest_size"] = file_stats["largest_size"]
                    stats ["largest_file"] = file_stats ["largest_file"]
                stats["file_count"]+= file_stats["file_count"]
                stats["total_lines"]+=file_stats["total_lines"]
                stats["total_characters"]+=file_stats["total_characters"]
            if path_name.endswith(".txt"):
                stats["file_count"]+=1
                with open(
                    current_path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                    ) as file :
                    file_size = len(file.read())
                    if stats["largest_size"] < file_size :
                        stats["largest_size"] = file_size
                        stats["largest_file"] = current_path
                    stats["total_characters"] +=file_size
                    file.seek(0)
                    for file_line in file:
                        stats ["total_lines"]+=1
                       


    except PermissionError :
         print("Access denied:",path)

    return stats


path = input("Write folder path: ")


print (
search(path))