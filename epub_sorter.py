import time
start_time = time.time()

from ebooklib import epub
from shutil import copy2

import os


errCount = 0
rawFileCount = 0
fileCount = 0
double = 0

baseDir = "./rawEbooks"
targetDir = "./sorted_epub/"

for root, dirs, files in os.walk(baseDir, topdown=True):
   for rawName in files:
      if rawName[-5:] == ".epub":
         rawFileCount += 1
         #print("File:", rawName)
         try:
            book = epub.read_epub(os.path.join(root, rawName))
            author = book.get_metadata('DC', 'creator')[0][0]
            title = book.get_metadata('DC', 'title')[0][0]
            #print("   Raw creator:", author)
            if "," in author:
               author_split = author.split(",")
               firstName = author_split[1]
               if firstName[0] == " ":
                  firstName = firstName[1:]
               lastName = author_split[0]
               author = firstName + " " + lastName
            doubleSpace = author.find("  ")
            if doubleSpace != -1:
               author = author[:doubleSpace] + author[doubleSpace + 1:]
            #print("   Title:", title)
            #print("   Author:", author)
            dir = targetDir + author
            #print("   Dir", dir)
            if os.path.isdir(dir):
               pass
            else:
               os.mkdir(dir)
            fileName = author + " [" + title + "].epub"
            #print("   File Name:", fileName)
            #print(dir + fileName)
            if os.path.isfile(dir + "/" + fileName):
               double += 1
               pass
            else:
               copy2(os.path.join(root, rawName), dir + "/" + fileName)
               fileCount += 1
         except Exception as e:
            print("file: " + rawName)
            print("error", e)
            copy2(os.path.join(root, rawName), targetDir + "000_ignored_files/" + rawName)
            print("")
            errCount += 1
         #print("")

print("Raw Files count: " + str(rawFileCount))
print("Error count: " + str(errCount))
print("Files count: " + str(fileCount))
print("Double ignored: " + str(double))
print("--- %s seconds ---" % (time.time() - start_time))
