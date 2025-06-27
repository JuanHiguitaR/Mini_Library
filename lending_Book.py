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


def menu() -> str:
    print("📚===Welcome to library system===📚")
    print(" 1. Register a book")
    print(" 2. Register a customer")
    print(" 3. Lending a book")
    print(" 4. Return a book")
    print(" 5. Status lending books")
    print(" 0. Exit")
    print("📚===============================📚")
    return input("Enter a valid option (0-5): ")


def book_Record():
    pass


def customer_Record():
    pass


def lend_book():
    pass


def return_Book():
    pass


def borrow_Status():
    pass


if __name__ == "__main__":
    main()
