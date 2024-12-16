import re


def customer():
    print("\n1. Login")
    print("2. Sign In")

    try:
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            login()
        elif choice == 2:
            signin()
        else:
            print("\nInvalid selection. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")





def login():
    name = input("Enter your name: ")
    while True:
        phone_number = input("\nEnter your phone number: ")
        if re.match(r'^\d{10}$', phone_number):
            break
        else:
            print("\nInvalid phone number. It must be a 10-digit number.")
       

    
    while True:
        new_password = input("\nEnter your new password: ")
    
        if len(new_password) < 8:
            print("Password must contain at least 8 characters.")
        elif re.search("[!@#$%&^*]", new_password) is None:
            print("Password must have at least 1 special characters.")
        elif re.search("[A-Z]", new_password) is None:
            print("Password must have at least 1 capital letter.")
        elif re.search("[a-z]", new_password) is None:
            print("Password must have at least 1 lowercase letter.")
        elif re.search("[0-9]", new_password) is None:
            print("Password must have at least 1 number.")
        else:
            print("Valid Password!")

        confirm_password = input("\nRe-enter your password: ")

        if new_password == confirm_password:
            print("\nYour account has been created successfully.")
            customer_dashboard(name)
            break
        else:
            print("Passwords do not match. Please try again.")


def signin():
    username = input("Enter username: ")
    password = input("Enter your password: ")
    
    
    while True:
        phone_number = input("Enter your phone number: ")
        if re.match(r'^\d{10}$', phone_number):
            break
        else:
            print("Invalid phone number. It must be a 10-digit number. please try again")
        

    print(f"Welcome back, {username}!")
    customer_dashboard(username)


def customer_dashboard(username):
    print(f"\nHello, {username}! Welcome to Ram Cinemas")
    
    print("\n1. View Movies")
    print("2. Logout")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice==1:
                movies_list()
                break
            elif choice==2:
                exit_program()
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        



def movies_list():
    print("\nTHIS WEEK MOVIES:")
    print("1. Kanguva")
    print("2. Amaran")
    print("3. Lucky Baskar")

    
    choice=int(input("\nenter your choice: "))
    if choice==1:
        kanguva()
    elif choice==2:
        amaran()
    elif choice==3:
        lucky_baskar()
    else:
        print("invalid choice, please try again ")



def kanguva():
    print("\nMovie Name: KANGUVA")
    print("Genre: Historical Adventure")
    print("IMDB Rating: 5/10")
    print("\n1. BOOK YOUR SEATS")

def amaran():
    print("\nMovie Name: AMARAN")
    print("Genre: Biopic")
    print("IMDB Rating: 9/10")
    print("\nBOOK YOUR SEATS (Coming Soon!)")

def lucky_baskar():
    print("\nMovie Name: LUCKY BASKAR")
    print("Genre: crime, drama, and thriller")
    print("IMDB Rating: 9/10")
    print("\nBOOK YOUR SEATS (Coming Soon!)")


def admin():
    print("\nlogin to admin Section")
    admin_id = input("Enter your admin ID: ")
    password = input("Enter your password: ")

    if admin_id == "1001" and password == "balaji":
        add_movies()
    else:
        print("Invalid admin ID or password.")


def add_movies():
    print("\nADD MOVIES.")

    movie_name = input("Enter the new movie name: ")
    runtime = input(f"Enter the runtime for {movie_name} (in minutes): ")
    screen = input(f"Enter the screen for {movie_name}: ")
    print(f"\nMovie '{movie_name}' details updated successfully.")


def exit_program():
    print("Thank you for visiting Ram Cinemas. Goodbye!")


# Main Program
while True:
    print("\nWelcome to Ram Cinemas")
    print("\n1. Admin")
    print("2. Customer")
    print("3. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            admin()
        elif choice == 2:
            customer()
        elif choice == 3:
            exit_program()
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
