import os
import filecmp

#Path to directory containing files

directory = 'D:\\software_tests\\test_automation_upcoming\\test\\architecture\\iss\\star12\\s12_tc-23\\misc\\'

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
                    if os.path.getsize(path_tc) != os.path.getsize(path): #if size of files is not the same
                        print ('%s = SIZE DOES NOT MATCH <-------' % filename)
                        diff_list.append(filename)
                        falsecnt += 1
                        continue
                    else:
                        if f1.read() == f2.read():
                            truecnt += 1
                        else: 
                            print ('%s = FALSE <-------' % filename)
                            diff_list.append(filename)
                            falsecnt += 1
                        
                        
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
        