from isbnlib import meta, isbn_from_words, info, get_isbnlike
from isbnlib.registry import bibformatters
import pandas as p

#.replace('{', '').replace('}', '').replace(',', '')
print("Enter ISBN's")
isbnInput = input()
isbnList = get_isbnlike(isbnInput, level = 'normal')
linkList = []
SERVICE = "openl"
link = "https://www.amazon.com/s?k=9780030368165&crid=3JNVDULVN4JTX&sprefix=9780071600637%2Caps%2C65&ref=nb_sb_noss"
bibtex = bibformatters["bibtex"]
counter = 1

for isbn in isbnList:
    newLink = link.replace(isbn_from_words(link), isbn)
    linkList.append(newLink)
    try:
        print(bibtex(meta(isbn, SERVICE)).replace('{', '').replace('}', '').replace(',', ''))
    except Exception:
        print("Bok no foun, be ded")
    print(info(isbn))
    print("Price: ")
    print('--------------------------------------------------------------------------------')

for vi in linkList:
    print(f'{counter}: {vi}')
    counter += 1

linkList.clear()

    
    
# from isbnlib import meta, isbn_from_words, info, get_isbnlike
# from isbnlib.registry import bibformatters
# import pandas as p

# #.replace('{', '').replace('}', '').replace(',', '')
# print("Enter ISBN's")
# isbnInput = input()
# isbnList = get_isbnlike(isbnInput, level = 'normal')
# records = []
# rows= []
# SERVICE = "openl"
# link = "https://www.amazon.com/s?k=9780030368165&crid=3JNVDULVN4JTX&sprefix=9780071600637%2Caps%2C65&ref=nb_sb_noss"
# bibtex = bibformatters["bibtex"]

# for isbn in isbnList:
#     row = {}
#     for node in isbnList:
#         row[node.tag] = node.text
    
#     rows.append(row)
#         # newLink = link.replace(isbn_from_words(link), isbn)
#         # print(newLink)
#         # print(bibtex(meta(isbn, SERVICE)).replace('{', '').replace('}', '').replace(',', ''))
#         # print(info(isbn))
#         # print('--------------------------------------------------------')

# df = p.DataFrame(rows)
# df.to_excel('bookList.xlsx')
    
    