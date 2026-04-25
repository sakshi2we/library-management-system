books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    books.append({"title": title, "author": author, "issued": False})
    print("Book added successfully!")

def view_books():
    if not books:
        print("No books available")
    else:
        for i, book in enumerate(books):
            status = "Issued" if book["issued"] else "Available"
            print(f"{i+1}. {book['title']} by {book['author']} - {status}")

def issue_book():
    view_books()
    index = int(input("Enter book number to issue: ")) - 1
    if 0 <= index < len(books):
        if not books[index]["issued"]:
            books[index]["issued"] = True
            print("Book issued successfully!")
        else:
            print("Book already issued")
    else:
        print("Invalid selection")

def return_book():
    view_books()
    index = int(input("Enter book number to return: ")) - 1
    if 0 <= index < len(books):
        if books[index]["issued"]:
            books[index]["issued"] = False
            print("Book returned successfully!")
        else:
            print("Book was not issued")
    else:
        print("Invalid selection")

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        break
    else:
        print("Invalid choice")