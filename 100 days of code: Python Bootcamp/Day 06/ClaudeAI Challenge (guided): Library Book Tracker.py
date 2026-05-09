# Library Book Tracker
# Build a program that manages a small library. Define these functions:

# show_books(books) — prints all books currently available
# borrow_book(books, title) — removes a book from the list if it exists, prints a message if it doesn't
# return_book(books, title) — adds a book back to the list

# Start with this list:

books = ["Dune", "1984", "The Martian", "Foundation", "Brave New World"]

# Then use a while loop menu:
# 1. Show available books
# 2. Borrow a book
# 3. Return a book
# 4. Exit

# Start with Step 1 — define show_books and call it. Tell me what you have when ready.
#Claude gave me a hint to use enumerate

def show_books(books):
    for index, book in enumerate(books, 1):
        print(f"{index}. {book}")

# show_books(books)

# Now — Step 2: define borrow_book(books, title). 
# It should remove a book from the list if it exists, and print a message if it doesn't. Think about what list method could remove an item by value.

def borrow_books(books, title):
    if title in books:
        books.remove(title)
        print(f"Thank you for your choice!\nBelow, you can find the updated list of the remaining books: ")
        show_books(books)
    else:
        print("Either this book has been borrowed already, or does not exist")

# Now Step 3: define return_book(books, title) — adds a book back to the list. Think about what list method adds an item.

def return_book(books, title):
    books.append(title)
    print(f"Thank you very much for returning this book!\nBelow, you can find the updated list of the remaining books: ")
    show_books(books)

# Now Step 4: build the while loop menu combining all three functions. Same pattern as the ATM.

power = True
print("Welcome to the Celestial Library of Milky Way (We are better than Andromeda ;)")

while power:
    print("1. Show available Books\n2. Borrow a book\n3. return a book\n4. Turn off")
    user_choice = int(input("Which option do you need?"))
    if user_choice == 1:
        print("-------")
        show_books(books)
        print("-------")
    elif user_choice == 2:
        print("-------")
        user_books_to_borrow = input("Which book?")
        borrow_books(books, user_books_to_borrow)
        print("-------")
    elif user_choice == 3:
        print("-------")
        user_books_to_return = input("What book?")
        return_book(books, user_books_to_return)
        print("-------")
    elif user_choice == 4:
        power = False
