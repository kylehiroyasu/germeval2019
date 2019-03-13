from bs4 import BeautifulSoup
import pandas as pd

def bs_book_to_dict(book):
    return {
        'book_date':book['date'],
        'lang':book['xml:lang'],
        'copyright':book.copyright.text,
        'categories':list(book.categories.stripped_strings),
        'title':book.title.text,
        'description':list(book.stripped_strings)[1],
        'authors':book.authors.text,
        'published_date':book.published.text,
        'isbn':book.isbn.text,
        'url':book.url.text
    }


def books_to_df(books):
    books_list = []
    for book in books.childGenerator():
        if len(book) > 1:
            books_list.append(bs_book_to_dict(book))
    book_df = pd.DataFrame(books_list)
    return book_df

