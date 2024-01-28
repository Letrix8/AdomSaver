import time 
import glob
import os
import shutil


currentFolder = 'C:/Work/Code/AdomSaverOld/Current'             #Replace with ADOM save folder
backupFolder = 'Stored'                                         #Backup folder
charName = 'test'                                               #Char name
currsave = currentFolder + '/' + charName + '.svg' 
bkpsave = backupFolder + '/' + charName + '.svg'

#iteration = 0

while True:
    #print('Iteratin number ', iteration)
    
    if (~len(glob.glob(bkpsave)) & len(glob.glob(currsave))):
        shutil.copyfile(currsave, bkpsave)
    elif (~len(glob.glob(currsave)) & len(glob.glob(bkpsave))):
        shutil.copyfile(bkpsave, currsave)
    elif (len(glob.glob(bkpsave)) & len(glob.glob(currsave))):
        currsave_mt = os.path.getmtime(currsave)
        bkpsave_mt = os.path.getmtime(bkpsave)
        if currsave_mt > bkpsave_mt:
            shutil.copyfile(currsave, bkpsave)
           
    time.sleep(2) 
    #iteration+=1