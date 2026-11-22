import os 

def find_dup(folder_path):
    files ={}
    dup_file={}
    check_files=[]
    all_d=0
    for paths in os .listdir(folder_path):
        newpath = os.path.join(folder_path,paths)
        if os.path.isdir(newpath):
            continue
        
        try:
            with open(
                newpath,
                "rb"
                ) as f:
                    file_read = f.read()
                    files[paths] = file_read
        except PermissionError as e:
            print (e,"\n we cant help you ")                     

    for indecs1 , (key1, value1)  in enumerate(files.items()):
        if key1 in check_files:             
            continue
        
        for indecs2 , (key2, value2)  in enumerate(files.items()):
            

            if indecs2 > indecs1:

                if value1 == value2:
                    if key1 not in check_files:
                        dup_file.setdefault(f"group{indecs1}",[]).append(key1)
                        check_files.append(key1)   
                    dup_file[f"group{indecs1}"].append(key2)
                    check_files.append(key2)

    if not dup_file:
        return "We don't have any duplicate files"
    for key,indecs in dup_file.items():
        x  = len(indecs) -1
        all_d +=x
        dup_file[key].append(f"dups are {x}")
    dup_file["dups all are : "] = all_d
    return dup_file     
        
        
    
x = input("write a path")
print (find_dup(x))


                   
                    

                    


             
             