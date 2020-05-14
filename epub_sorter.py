import ebooklib
from ebooklib import epub

book = epub.read_epub('sample.epub')

print(book.get_metadata('DC', 'title'))
print(book.get_metadata('DC', 'creator'))
print(book.get_metadata('DC', 'identifier'))