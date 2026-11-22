import os 
from pathlib import Path
def replace(path_folder,replace_item,item):
    total_replaced=0
    total_txt = 0
    for paths in os.listdir(path_folder):
        newpath = os.path.join(path_folder,paths)
        if os.path.isdir(newpath):
            continue
        chek = Path(newpath)

        if chek.suffix.lower() == ".txt":
            total_txt+=1
            try:
                with open(newpath,
                      "r",
                      encoding="utf-8",
                      errors="ignore"
                      )as file:
                    text = file.read()
            except PermissionError as a:
                print(f"we cant see your txt file \n {a}")
                continue
            if item in text:
                newtext = text.replace(item,replace_item)
                total_replaced += text.count(item)
        
                
                with open(newpath,
                      "w",
                      encoding="utf-8",
                      errors="ignore"
                      ) as file:
                        file.write(newtext)
                
                
            else:
                continue
    if total_replaced == 0 :
        print("we didnt find any thing")
    if total_txt == 0 :
        print("we dont have any txt ")
    return total_txt,total_replaced


                
