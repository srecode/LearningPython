import os

for folderName, subFolders, fileNames in os.walk('/Users/sampathk/test_python'):
    print ('Current folder is ' + folderName)

    for subFolder in subFolders:
        print ('Subfolders if folder ' + folderName + ': ' + subFolder)

    for fileName in fileNames:
        print ('files inside ' + folderName + ': ' + fileName)

    print(' ')