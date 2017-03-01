import os

#Base path to directory containing files
path = 'D:\\base_directory\\'

#init variables
subpath = ''
filelist = []
output = ''

expr = 'BFINS' #what to look for

dirs = next(os.walk(path))[1] #list all directories in given path ([2] for files only)
dircnt = len(dirs)


print ("SCRIPT STARTED")

i = 1
for subdir in dirs: #iterate sub directories
    print ("Checking dir %i of %i" % (i,dircnt))
    
    
    subpath = path + subdir + '\\input\\' #in subdir, get into \input\ directory
    
    try:
        for filename in next(os.walk(subpath))[2]: #iterate files in subpath
            try:
                with open(subpath + filename,'r') as f1: #open file
                    for line in f1:        #iterate file line by line
                        if expr in line:    #if expression has been found...
                            filelist.append(subpath+filename) #append filename to filelist
                            break;
                    
            except:
                print ("Error! Filename: %s" %filename)
    except:
        print ("Unknown error!")
    i = i + 1


#save found file paths containing expression to a newfile
with open(path + "searchResult.txt",'w') as fileOut:
    output = '\n'.join(filelist)
    fileOut.write(output)
    print ("\nSaved to file succesfully!")
    print ("Path: %ssearchResult.txt" % path) 
    
    
print ("SCRIPT FINISHED")