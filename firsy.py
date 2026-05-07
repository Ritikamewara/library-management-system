books = []

def add_book():
    name = input("Enter book name: ")
    books.append(name)
    print("Book added!")

def view_books():
    if not books:
        print("No books available")
    else:
        print("Books in library:")
        for b in books:
            print("-", b)

def delete_book():
    name = input("Enter book name to delete: ")
    if name in books:
        books.remove(name)
        print("Book deleted")
    else:
        print("Book not found")

while True:
    print("\n1.Add  2.View  3.Delete  4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice")