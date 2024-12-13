import re


def customer():
    print("1. Login")
    print("2. Sign In")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            login()
        elif choice == 2:
            signin()
        else:
            print("Invalid selection. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")





def login():
    name = input("Enter your name: ")
    while True:
        phone_number = input("Enter your phone number: ")
        if re.match(r'^\d{10}$', phone_number):
            break
        else:
            print("Invalid phone number. It must be a 10-digit number.")
       

    new_password = input("Enter your new password: ")
    confirm_password = input("Re-enter your password: ")

    if new_password == confirm_password:
        print("Your account has been created successfully.")
        customer_dashboard(name)
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

    
    choice = int(input("Enter your choice: "))
    if choice==1:
        movies_list()
    elif choice==2:
        print("log out")
    else:
        print("invalid choice, please try again")



def movies_list():
    print("\nTHIS WEEK MOVIES:")
    print("1. Kanguva")
    print("2. Amaran")
    print("3. Lucky Baskar")

    choice=int(input("enter your choice: "))
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
    print("1. BOOK YOUR SEATS")

def amaran():
    print("\nMovie Name: AMARAN")
    print("Genre: Biopic")
    print("IMDB Rating: 9/10")
    print("BOOK YOUR SEATS (Coming Soon!)")

def lucky_baskar():
    print("\nMovie Name: AMARAN")
    print("Genre: Biopic")
    print("IMDB Rating: 9/10")
    print("BOOK YOUR SEATS (Coming Soon!)")


def admin():
    admin_id = input("Enter your admin ID: ")
    password = input("Enter your password: ")

    if admin_id == "1001" and password == "balaji":
        add_movies()
    else:
        print("Invalid admin ID or password.")


def add_movies():
    movie_name = input("Enter the new movie name: ")
    runtime = input(f"Enter the runtime for {movie_name} (in minutes): ")
    screen = input(f"Enter the screen for {movie_name}: ")
    print(f"Movie '{movie_name}' details updated successfully.")


def exit_program():
    print("Thank you for visiting Ram Cinemas. Goodbye!")


# Main Program
while True:
    print("\nWelcome to Ram Cinemas")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))
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
