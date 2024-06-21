import tkinter as tk
from tkinter import simpledialog
from isbnlib import meta, isbn_from_words, info, get_isbnlike, config, registry
from isbnlib.registry import bibformatters



def isbnlookup(isbnInput):
    isbnList = get_isbnlike(isbnInput, level='normal')
    linkList = []
    SERVICE = "openl"
    SERVICE2 = 'goob'
    SERVICE3 = 'wiki'
    services = [SERVICE, SERVICE2, SERVICE3]
    link = "https://www.amazon.com/s?k=9780030368165&crid=3JNVDULVN4JTX&sprefix=9780071600637%2Caps%2C65&ref=nb_sb_noss"
    bibtex = bibformatters["bibtex"]
    counter = 1

    for isbn in isbnList:
        newLink = link.replace(isbn_from_words(link), isbn)
        linkList.append(newLink)
        for index, i in enumerate(services):  
            try:
                print(bibtex(meta(isbn, service = i)).replace('{', '').replace('}', '').replace(',', ''))
                print(f'{counter}):')
                print(f'Service Used: {i}')
            except Exception as e:
                if index == len(services)-1:
                    print(f'Book was not found: {e}')
                continue
            else:
                print(info(isbn))
                print("Price: ")
                print('--------------------------------------------------------------------------------')
                break
        

    for vi in linkList:
        counter = 1
        print(f'{counter}: {vi}')
        counter += 1



def main(isbnInput):
    isbnlookup(isbnInput)



if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    isbnInput = simpledialog.askstring("Input", "Copy and paste email, or just ISBN's into window:")

    if isbnInput:
        main(isbnInput)
    else:
        print("No ISBNs provided.")

    input("Press Enter to exit...")  # Keeps the terminal open
