# Here has a globals variables
books = []
customers = []
number = 0


# Create def main to start the aplication. Inside has a option that connect with the functions.
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


# This function show menu and return the option, customer enter string
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


# this function create a id's to customers, it's connected with customer_Record() function
def random_Id():
    global number
    while True:
        number += 1
        id = f"Soc-{number:03d}"
        yield id


# This function create a new book at the book list
def book_Record():
    global books
    print("📖===Create a new book===📖")
    title = input("Enter a book title: ")
    author = input("Enter a book author: ")
    isbn = input("Enter a ISBN for book: ")
    books.append(
        {"Title": title, "Author": author, "ISBN": isbn, "Status": "available"}
    )
    print("Book List update sucessful!✅")


# This function create a new customer at the customer list
def customer_Record():
    global customer
    print("🤓===Create a new Customer===🤓")
    name = input("Enter full name: ")
    phone_Number = input("Enter Phone number: ")
    automatic_Id = next(random_Id())
    customers.append({"Name": name, "Phone": phone_Number, "Customer": automatic_Id})
    print("New customer add sucessful!✅")


# This function take parameters and check it's exist in a list and change status book for
# unavailabe
def lend_book():
    book_ISBN = input("Enter book ISBN: ")
    for book in books:
        if book["ISBN"] == book_ISBN:
            customer_id = input("Enter customer id (Soc-number): ")
            for customer in customers:
                if customer["Customer"] == customer_id:
                    book["Status"] = "Unavalible"
                    print(
                        f"The status unavailable change for book {book["Title"]} Sucessful!✅ "
                    )
                else:
                    print("❌ Customer doen't exist! ")
        else:
            print("❌ Book doesn't exist! ")


def return_Book():
    pass


def borrow_Status():
    print(books)


if __name__ == "__main__":
    main()
