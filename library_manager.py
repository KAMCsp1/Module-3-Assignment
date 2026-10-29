from book import Book


def add_book(library):
    
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")

    new_book = Book(title, author, isbn)
    library.append(new_book)

    print("Book added successfully!")


def list_books(library):
    
    if not library:
        print("The library is empty.")
        return

    print("\nBooks in Library:")

    for book in library:
        print(book)


def find_book(library, query):
    
    query = query.lower()

    for book in library:
        if (
            query == book.title.lower()
            or query == book.author.lower()
        ):
            return book

    return None


def main():
    my_library = []

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Find Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(my_library)

        elif choice == "2":
            list_books(my_library)

        elif choice == "3":
            query = input("Enter book title or author: ")
            book = find_book(my_library, query)

            if book:
                print("Book found:")
                print(book)
            else:
                print("Book not found.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
