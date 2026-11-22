import os 
from pathlib import Path
import shutil
def movefile(path_file):
    text_folder=None
    text_folder_path=None
    chek = os.listdir(path_file)
    num_of_move = 0
    for item in chek:
        if item.lower() == "text_files":
            text_folder_path=os.path.join(path_file,item)
            if os.path.isdir(text_folder_path):
                text_folder = item
    if text_folder is None:
        text_folder = "text_files"
        text_folder_path =os.path.join(path_file,text_folder)
        os.mkdir(os.path.join(path_file,text_folder))

    try:
        for paths in os.listdir(path_file):
            newpath = os.path.join(path_file,paths)
            if os.path.isdir(newpath):
                continue
            chek2 = Path(paths)
            if chek2.suffix.lower() == ".txt":
                newpath3 = os.path.join(text_folder_path,paths)
                if not os.path.exists(newpath3):
                    
                    shutil.move(newpath,text_folder_path)
                    num_of_move+=1

    except Exception as e:
        print("you can't move",e)   
    return num_of_move 
pathfile=input("enter the path: ")
print("file you move: ",movefile(pathfile))

            
            
        
        
        
        

        