import ebooklib
from ebooklib import epub

import os
for root, dirs, files in os.walk("./epub_sample", topdown=True):
   for name in files:
      if (name[-5:] == ".epub"):
         print("File:", name)
         try:
            book = epub.read_epub(os.path.join(root, name))
            print("   Title:", book.get_metadata('DC', 'title')[0][0])
            print("   Author:", book.get_metadata('DC', 'creator')[0][0])
         except:
            print("Error")