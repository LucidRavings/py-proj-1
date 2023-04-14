### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def add_book():
#     title = input("Title of your book:")
#     author = input("Author of your book:")
#     year = input("The year the book was published:")
#     rating = input("Rate this book with a number from 1 to 5:")
#     pages = input("Number of pages in this book:")


### Step 2 - Type conversion

## Now convert the proper data-types from strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def add_book():
#     title = input("Title of your book:")
#     author = input("Author of your book:")
#     year = int(input("The year the book was published:"))
#     rating = float(input("Rate this book with a number from 1 to 5:"))
#     pages = int(input("Number of pages in this book:"))

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
# def add_book():
#     title = input("Title of your book:")
#     author = input("Author of your book:")

#     try:
#         year = int(input("The year the book was published:"))
#     except:
#         year = int(input("Use only numbers please:"))

#     try:
#         rating = float(input("Rate this book with a number from 1 to 5:"))
#     except:
#         rating = float(input("Use only numbers please:"))

#     try:
#         pages = int(input("Number of pages in this book:"))
#     except:
#         pages = int(input("Use only numbers please:"))


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

# def main_menu():

#     option = input("\nType 1 to run option 1.\nType 2 to run option 2.\nType 3 to run option 3.")

#     if option == "1":
#         print("option 1 ran!")
#     elif option == "2":
#         print("option 2 ran!")
#     elif option == "3":
#         print("option 3 ran!")
#     else:
#         print("Failed to run any options, please Type 1, 2, or 3.")


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

my_library = [
    {
        "title": "Eragon",
        "author": "Christopher Paolini",
        "year": 2003,
        "rating": 5.0,
        "pages": 509
    },
    {
        "title": "Elminster: The Making of a Mage",
        "author": "Ed Greenwood",
        "year": 1994,
        "rating": 4.4,
        "pages": 336
    },
    {
        "title": "Ender's Game",
        "author": "Orson Scott Card",
        "year": 1985,
        "rating": 4.41,
        "pages": 324
    },
    {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "year": 2008,
        "rating": 4.32,
        "pages": 374
    }
]

def add_book():
    title = input("Title of your book:")
    author = input("Author of your book:")

    try:
        year = int(input("The year the book was published:"))
    except:
        year = int(input("Use only numbers please:"))

    try:
        rating = float(input("Rate this book with a number from 1 to 5:"))
    except:
        rating = float(input("Use only numbers please:"))

    try:
        pages = int(input("Number of pages in this book:"))
    except:
        pages = int(input("Use only numbers please:"))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    
    return book_dictionary

def print_book_list(library):
    for book in library:
        title = book["title"]
        author = book["author"]
        year = book["year"]
        rating = book["rating"]
        pages = book["pages"]

        print(f"{title} by {author} | published in {year} | {rating}/5.0 | {pages} pages long.")

def main_menu(library):

    waiting = True

    while waiting:
        option = input("\nType 1 to add a book to your library.\nType 2 to list all books in your library.\nType 3 to quit.\nType here:")

        if option == "1":
            library.append(add_book())
            print("\nBook added!")
        elif option == "2":
            print_book_list(library)
        elif option == "3":
            print("\nCome back soon!")
            waiting = False
        else:
            print("Failed to run any options, please Type 1, 2, or 3.")

main_menu(my_library)