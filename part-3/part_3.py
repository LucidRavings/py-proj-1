my_library = [
   {"title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
    },
   {"title": "Ender's Game",
    "author": "Orson Scott Card",
    "year": 1985,
    "rating": 4.41,
    "pages": 324
    },
   {"title": "Eragon",
    "author": "Christopher Paolini",
    "year": 2002,
    "rating": 5.00,
    "pages": 544
    }
]


my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_parser(book_dictionary):
    print(book_dictionary)
    title = book_dictionary["title"]
    author = book_dictionary["author"]
    year = book_dictionary["year"]
    pages = book_dictionary["pages"]
    rating = book_dictionary["rating"]
    book_string = f"{title} was written by {author} in {year}.  Is {pages} pages long, and has a rating of {rating}"
    return book_string
    

print(book_parser(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def book_name(book_dictionary):
    return book_dictionary["title"]

def book_author(book_dictionary):
    return book_dictionary["author"]

def book_year(book_dictionary):
    return book_dictionary["year"]

def book_pages(book_dictionary):
    return book_dictionary["pages"]

def book_rating(book_dictionary):
    return book_dictionary["rating"]

print(book_name(my_book))
print(book_author(my_book))
print(book_year(my_book))
print(book_pages(my_book))
print(book_rating(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

#Func 1: Count of all books in the library.

def library_book_count(book_library):
    book_count = 0
    for book_dictionary in book_library:
        book_count += 1
    
    return f"There are {book_count} books in this library"

print(library_book_count(my_library))
#Func 2: List the names of all books.

def get_set_of_books(book_library):
    book_name_set = set()

    for book_dictionary in book_library:
        book_name_set.add(book_dictionary["title"])

    return f"This library contains {book_name_set}"

print(get_set_of_books(my_library))
#Func 3: List the names of all books below a given page count.
def get_books_by_page(book_library, num):
    book_set = set()
    for book_dictionary in book_library:
        if book_dictionary["pages"] < num:
            book_set.add(book_dictionary["title"])
        
    return f"Books with less than {num} pages in this library {book_set}"

print(get_books_by_page(my_library,500))