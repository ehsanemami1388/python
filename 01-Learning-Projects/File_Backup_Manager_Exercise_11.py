import os 
from pathlib import Path
import shutil
def backup(folder_path):
    backup_f = os.listdir(folder_path)
    files_total = {
        "total_txtfile":0,
        "total_not_copy":0,
        "total_copy":0
    }
    new_backup = os.path.join(folder_path,"backup")
    backup_name = next((i for i in backup_f if i.lower() == "backup"),None)
    if backup_name:
        new_backup = os.path.join(folder_path, backup_name)
    else:
        new_backup2 = Path(new_backup)
        new_backup2.mkdir()
    for paths in os.listdir(folder_path):
        newpath2 = os.path.join(folder_path,paths)
        check = Path(newpath2)
        if os.path.isdir(newpath2):
            continue
        if check.suffix.lower() == ".txt":
            files_total["total_txtfile"]+=1
            
            if  paths in os.listdir(new_backup):
                files_total["total_not_copy"]+=1
                continue
                
            else:
                shutil.copy2(newpath2,new_backup)
                files_total["total_copy"]+=1
    if files_total["total_txtfile"] == 0:
        return "you dont have any file"
    else:
        return files_total


x = input("enter your path")
print(backup(x))

