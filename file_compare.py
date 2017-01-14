#############################################
## Compare pairs of two files (f1,f2) content. Count the number of exactly the same files (truecnt), 
## numbers of files that do not match (falsecnt) and numbers of files that are missing (nullcnt)


import os
import filecmp

#Path to directory containing files
directory = 'D:\\tests\\'

diff_list = []

nullcnt = 0
falsecnt = 0
truecnt = 0
i = 0

print ("\n\nTesting... \n")
print (directory)
print ("\n")

for filename in os.listdir(directory):
    if filename.startswith("dbg_hw_") and filename.endswith(".lst"): 
        path = directory + filename
        filename_tc = 'dbg_sim_' + filename.split('_')[2]
        path_tc = directory + filename_tc
        
        with open(path) as f1:
            try:
                with open(path_tc) as f2:
                    if f1.read() == f2.read():
                        # print ('%s = TRUE\n' % filename)
                        truecnt += 1
                        pass
                    else: 
                        print ('%s = FALSE <-------' % filename)
                        diff_list.append(filename)
                        falsecnt += 1
                        # break;
                        
            except:
                # print ('%s = NULL. SIM file does not exist!!!\n' % filename)
                nullcnt += 1
                
        i += 1
        continue
    else:
        continue
        
        
print ("PROGRAM FINISHED\n\n")
print ('Null count  = %d\n' % nullcnt)
print ('False count = %d\n' % falsecnt) 
print ('True count  = %d\n' % truecnt) 
print ('Total files processed  = %d\n' %i) 
        