### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

my_library = "library.txt"

def add_book(library):
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

    with open(library, "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

# add_book(my_library)

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

def print_book_list(library):
    with open(library, "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")

            print(f"{title} by {author} | published in {year} | {rating}/5.0 | {pages} pages long.")

# print_book_list(my_library)

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def print_book_count(library):
    count = 0
    with open(library, "r") as f:
        file = f.readlines()

        for line in file:
            count += 1
    print(f"There are {count} books in this library")

def print_total_page_count(library):
    count = 0
    with open(library, "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")
            page_number = int(pages)
            count += page_number
    print(f"There are {count} pages in your library")

def print_last_book(library):
    book = ""
    with open(library, "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")

            book = (f"{title} by {author} | published in {year} | {rating}/5.0 | {pages} pages long.")
    print(book)

def main_menu(library):

    waiting = True

    while waiting:
        option = input("\nType 1 to add a book to your library.\nType 2 to list all books in your library.\nType 3 to count the number of books in this library.\nType 4 to count the combined total of all books in your library.\nType 5 to see your most recently added book.\nType 0 to quit.\nType here:")

        if option == "1":
            add_book(library)
            print("\nBook added!")
        elif option == "2":
            print_book_list(library)
        elif option == "3":
            print_book_count(library)
        elif option == "4":
            print_total_page_count(library)
        elif option == "5":
            print_last_book(library)
        elif option == "0":
            print("\nCome back soon!")
            waiting = False
        else:
            print("Failed to run any options, please type a valid number")

if __name__ == "__main__":
    main_menu(my_library)