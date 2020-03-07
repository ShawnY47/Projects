#! python3
import os, shutil
##TargetList.txt is target list of sites, read file
file = open(os.path.relpath('TargetList.txt'))
TargetList = list(file.readlines())

##try to get rid of /n
for i in range(len(TargetList)):
    TargetList[i] = TargetList[i].strip('\n')

for folder in os.listdir(os.getcwd()):
    for site in TargetList:
        if os.path.isdir(folder):
            if folder == site:
                shutil.move(os.path.relpath(folder),os.path.join('backup',folder))
                print (folder + ' is move to ' + os.path.join('backup',folder))
