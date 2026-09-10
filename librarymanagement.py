class Books:
    def __init__(self, name, author, id):
        self.name = name
        self.author = author
        self.id = id
        self.available = True


book = []


class Library:

    def add(self):
        l = input("Enter book name: ")
        k = input("Enter author: ")
        e = int(input("Enter book ID: "))

        found = False

        for b in book:
            if b.id == e:
                found = True

        if found == True:
            print("ID already exists. Enter another book ID.")
        else:
            p = Books(l, k, e)
            book.append(p)
            print("Book added successfully")


    def issued(self):
        k = int(input("Enter the book ID: "))

        found = False

        for b in book:
            if b.id == k:
                found = True

                if b.available:
                    b.available = False
                    print("Book issued successfully")
                else:
                    print("Book is already issued")

        if found == False:
            print("Book not found")


    def show_books(self):
        if len(book) == 0:
            print("No books in the library")
        else:
            print("Books in Library:")

            for b in book:
                if b.available:
                    status = "Available"
                else:
                    status = "Issued"

                print(
                    "ID:", b.id,
                    "Name:", b.name,
                    "Author:", b.author,
                    "Status:", status
                )


    def search(self):
        o = int(input("Enter book ID: "))

        found = False

        for b in book:
            if b.id == o:
                print("Book found")
                print("Name:", b.name)
                print("Author:", b.author)
                found = True

        if found == False:
            print("Book not found")


    def retur(self):
        k = int(input("Enter the book ID: "))

        found = False

        for b in book:
            if b.id == k:
                found = True

                if b.available == False:
                    b.available = True
                    print("Book returned successfully")
                else:
                    print("Book was not issued")

        if found == False:
            print("Book not found")


# Create Library object
lib = Library()


# Menu
while True:

    print(" LIBRARY MANAGEMENT SYSTEM ")
    print("1. Add book")
    print("2. Search book")
    print("3. Issue book")
    print("4. Return book")
    print("5. Display all books")
    print("6. Exit")

    q = int(input("Enter your choice: "))

    if q == 1:
        lib.add()

    elif q == 2:
        lib.search()

    elif q == 3:
        lib.issued()

    elif q == 4:
        lib.retur()

    elif q == 5:
        lib.show_books()

    elif q == 6:
        print("Exiting the library...")
        break

    else:
        print("Invalid choice")