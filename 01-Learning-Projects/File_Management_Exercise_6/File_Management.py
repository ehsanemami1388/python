import os
import pathlib 
def file_managment(path_file,type_file):
    num=[]
    ntype_file= type_file.lower()
    try:
        for paths in os.listdir(path_file):
            
            newpath = os.path.join(path_file,paths)
            if os.path.isdir(newpath):
                            continue
            test = pathlib.Path(newpath)
            if test.exists():
                  if test.suffix.lower()==ntype_file:
                        test.unlink()
                        num.append(test)
           
        tedad =len(num)
        
        return os.listdir(path_file),num,tedad
    except:
        print ("error")    
path_file = input("please enter folder path: ")   
type_file = input("please enter type file that you want to delet: ")
natige = file_managment(path_file,type_file)
print (natige)
    
            