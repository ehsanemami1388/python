import os 
from pathlib import Path 
def file_statistic(folder_path):
    File_Statistics ={}
    total_file=0
    if not os.listdir(folder_path):
        return "folder is empty"
    for paths in os.listdir(folder_path):
        new_path = os.path.join(folder_path,paths)
        if os.path.isdir(new_path):
            continue
        path1 = Path(paths)
        if os.path.isfile(new_path):
            extension = path1.suffix.lower()
            total_file+=1
            if extension:
                
                if extension in File_Statistics:
                    File_Statistics[extension] +=1
                else:
                    File_Statistics[extension] = 1
            else:
                
                if  "No extention"in File_Statistics:
                    File_Statistics["No extention"]+=1
                else:
                    File_Statistics["No extention"]=1
                     
    total_extensions=len(File_Statistics)
    list_p = [File_Statistics,total_extensions,total_file]
    return list_p

x = input("enter a path :")
print (file_statistic(x))
    
                
