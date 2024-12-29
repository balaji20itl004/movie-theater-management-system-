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
    for a,m in enumerate(movies, start=1):
        print(f"{a}. {m['Name']}")

    
    print("select a movie to book tickets by entering the number.")
    choice = int(input("Enter your choice or press 0 to exit: "))
    
    try:
        if choice == 0:
            print("Exiting...")
        elif 1 <= choice <= len(movies):
            book_ticket(choice - 1)  
        else:
            print("Invalid choice! Please try again.")
    except ValueError:
        print("Invalid input! Please enter a number.")


def book_ticket(movie_index):
    movie= movies[movie_index]
    print(f"you selected: {movie['Name']}")
    available_seats = movie['Seat availability']
    print(f"Available seats: {available_seats}")

    try:
        num_tickets=int(input("Enter the number of tickets book: "))
        if 0 <num_tickets <=available_seats:
            a= available_seats - num_tickets
            print(f"Successfully booked {num_tickets} tickets for {movie['Name']}")
            print(f"Remaining seats: {a}")
        else:
            print("invalid number of tickets ! please try again")
    except ValueError:
        print("Inavlid input ! please enter valid number.")




    
           
    



movies=[]

def add_movies():
    print("\nADD MOVIES.")

    a=int(input("enter How much movies add: "))
    for i in range(a):
        movie_name = input("\nEnter the new movie name: ")
        runtime = input(f"Enter the runtime for {movie_name} (in minutes): ")
        screen = input(f"Enter the screen for {movie_name}: ")
        genre= input(f"Enter the genre for {movie_name}: ")
        imdb=input(f"Enter the IMDB Rating for {movie_name}: ")
        while True:
            try:
                seat = int(input(f"Set seat availability for {movie_name} (max 100 seats): "))
                if seat >= 0 and seat<=100:
                    break
                elif seat>=100:
                    print("only 100 seats alloted")
                else:
                    print("Seats must be a positive number.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        movies.append({"Name":movie_name, "Genre":genre, "RunTime":runtime, "screen":screen, "IMDB Rating":imdb, "Seat availability":seat})


        print(f"\nMovie '{movie_name}' details updated successfully.")

    print(f"updated movie list.")
    for a,m in enumerate(movies, start=1):
        print(f"{a}. {m['Name']}")
        break



def admin():
    print("\nlogin to admin Section")
    admin_id = input("Enter your admin ID: ")
    password = input("Enter your password: ")

    if admin_id == "1001" and password == "balaji":
        add_movies()
    else:
        print("Invalid admin ID or password.")





def exit_program():
    print("Thank you for visiting Ram Cinemas. Goodbye!")




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
