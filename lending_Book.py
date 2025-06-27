# Here has a globals variables
books = []
customer = []
number = 0


# Create def main to start the aplication. Inside has a Menu.
def main():
    while True:
        match menu():
            case "1":
                book_Record()
            case "2":
                customer_Record()
            case "3":
                lend_book()
            case "4":
                return_Book()
            case "5":
                borrow_Status()
            case "0":
                print("System closing.......🖥️")
                print("Thanks for used!👌🏻")
                break
            case _:
                print("❌ Invalid option")


# This function show menu and return the option customer select with string
def menu() -> str:
    """
    function to show menu and take an option.

    :return:
        str: Return a number with string format
    """
    print("📚===Welcome to library system===📚")
    print(" 1. Register a book")
    print(" 2. Register a customer")
    print(" 3. Lending a book")
    print(" 4. Return a book")
    print(" 5. Status lending books")
    print(" 0. Exit")
    print("📚===============================📚")
    return input("Enter a valid option (0-5): ")


def random_Id():
    global number
    while True:
        number += 1
        id = f"Soc-{number:03d}"
        yield id


def book_Record():
    global books
    print("📖===Create a new book===📖")
    title = input("Enter a book title: ")
    author = input("Enter a book author: ")
    isbn = input("Enter a ISBN for book: ")
    books.append({"Title": title, "Author": author, "ISBN": isbn})
    print("Books List update sucessful!✅")


def customer_Record():
    global customer
    print("🤓===Creater a new Customer===🤓")
    name = input("Enter full name: ")
    phone_Number = input("Enter Phone number: ")
    automatic_Id = next(random_Id())
    customer.append({"Name": name, "Phone": phone_Number, "Customer": automatic_Id})


def lend_book():
    pass


def return_Book():
    pass


def borrow_Status():
    print(customer)


if __name__ == "__main__":
    main()
