import ebooklib
from ebooklib import epub

import os
for root, dirs, files in os.walk("./epub_sample", topdown=True):
   for name in files:
      if (name[-5:] == ".epub"):
         print("File:", name)
         try:
            book = epub.read_epub(os.path.join(root, name))
            author = book.get_metadata('DC', 'creator')[0][0]
            title = book.get_metadata('DC', 'title')[0][0]
            print("   Title:", title)
            print("   Author:", author)
            dir = "./sorted_epub/" + author
            print(dir)
            if os.path.isdir(dir):
               pass
            else:
               os.mkdir(dir)
         except:
            print("error")