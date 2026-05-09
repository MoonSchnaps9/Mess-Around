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
#Claude gave me a hint to use enumarate

def show_books(books):
    for index, book in enumerate(books, 1):
        print(f"{index}. {book}")

show_books(books)