from ebooklib import epub
from shutil import copy2

import os

errCount = 0

for root, dirs, files in os.walk("./epub_sample", topdown=True):
   for name in files:
      if (name[-5:] == ".epub"):
         print("File:", name)
         try:
            book = epub.read_epub(os.path.join(root, name))
            author = book.get_metadata('DC', 'creator')[0][0]
            title = book.get_metadata('DC', 'title')[0][0]
            print("   Raw creator:", author)
            if ("," in author):
               author_split = author.split(",")
               firstName = author_split[1]
               if (firstName[0] == " "):
                  print("   Pop1")
                  firstName = firstName[1:]
               lastName = author_split[0]
               author = firstName + " " + lastName
            doubleSpace = author.find("  ")
            if (doubleSpace != -1):
               print("   Pop2")
               author = author[:doubleSpace] + author[doubleSpace + 1:]
            print("   Title:", title)
            print("   Author:", author)
            dir = "./sorted_epub/" + author
            print("   Dir", dir)
            if os.path.isdir(dir):
               pass
            else:
               os.mkdir(dir)
            fileName = author + " [" + title + "].epub"
            print("   File Name:", fileName)
            if os.path.isfile(fileName):
               pass
            else:
               copy2(os.path.join(root, name), dir + "/" + fileName)
         except Exception as e:
            print("error", e)
            errCount += 1
         print("")

print("Error count: " + str(errCount))