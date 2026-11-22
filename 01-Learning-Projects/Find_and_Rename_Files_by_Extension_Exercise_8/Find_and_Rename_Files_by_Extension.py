import os 

import pathlib
def find_and_change_name(path_folder,file_Extention):
    number_of_renames=1
    number_of_renames3=1
    file_Extention1=str(file_Extention)
    for path_files in os.listdir(path_folder):
        newpath=os.path.join(path_folder,path_files)
        if os.path.isdir(newpath):
            continue
        check = pathlib.Path(path_files)
        if check.suffix.lower() == file_Extention1.lower() :
            number_of_renames2=f"renamed_{number_of_renames}"
            Exception1 =number_of_renames2+ os.path.splitext(newpath)[1]
            newpath2=os.path.join(path_folder,Exception1)
            while  os.path.exists(newpath2):
                number_of_renames+=1
                number_of_renames2=f"renamed_{number_of_renames}"
                Exception1 =number_of_renames2+ os.path.splitext(newpath)[1]
                newpath2=os.path.join(path_folder,Exception1)
            try:
                os.rename(newpath,newpath2)
                number_of_renames +=1
                number_of_renames3+=1
            except Exception as e:
                print ("we can't help you because: ",e)
    if number_of_renames3 == 1:
        return f"we can't find any file with this extention {file_Extention1}"
    return number_of_renames3-1
pathfolder=input("enter your path: ")
extention_chang=input("enter extention that you want rename: ")
print(find_and_change_name(pathfolder,extention_chang))