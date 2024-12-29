import mysql.connector
import re
from tabulate import tabulate

connection=mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="root",
    database="ram_cinemas"


)



def customer():
    print("WELCOME TO RAM CINEMAS !")
    print("1.SIGN UP")
    print("2.SIGIN IN")
    print("3.VIEW MOVIES")
    print("4.EXIT")

    while True: 
        try:
            choice=int(input("enter your choice: "))
            if choice==1:
                customer_sign_up()
            elif choice==2:
                pass
            elif choice==3:
                pass
            elif choice==4:
                pass
            else:
                print("invalid choice, please try again")
        except ValueError:
            print("Invalid input, please enter only number")


def customer_sign_up():
    name=input("enter the name: ")
    while True:
        mobile=input("enter the mobile number: ")
        if re.match(r'^\d{10}$',mobile):
            break
        else:
            print("invalid mobile number, it must be 10 digit number")

    while True:
                password = input("\nEnter your new password: ")
    
                if len(password) < 8:
                    print("Password must contain at least 8 characters.")
                elif re.search("[!@#$%&^*]", password) is None:
                    print("Password must have at least 1 special characters.")
                elif re.search("[A-Z]", password) is None:
                    print("Password must have at least 1 capital letter.")
                elif re.search("[a-z]", password) is None:
                    print("Password must have at least 1 lowercase letter.")
                elif re.search("[0-9]", password) is None:
                    print("Password must have at least 1 number.")
                else:
                    print("Valid Password!")

                confirm_password = input("\nRe-enter your password: ")

                if password == confirm_password:
                    mycursor=connection.cursor()
                    sql="insert into customers (NAME, PHONE_NUMBER, PASSWORD) values (%s,%s,%s)"
                    users=(name,mobile,password)
                    mycursor.execute(sql,users)
                    connection.commit()
                    print("\nYour account has been created successfully.")
                    break
                else:
                    print("invalid")





def login():
    pass


def signin():
    pass


def customer_dashboard():
    pass
        



def movies_list():
  pass

    



def book_ticket(movie_index):
    pass



def add_movies():
   print("under development !")


def admin(admin_id,password):
    mycursor=connection.cursor()
    sql="insert into admin (ADMIN_ID,PASSWORD) values (%s,%s)"
    users=(admin_id,password)
    mycursor.execute(sql,users)
    connection.commit()
    print("\nYour account has been created successfully.")


def admin_page():
    while True:
        print("\nWELCOME TO RAM CINEMAS")
        print("1.ADMIN SIGN UP ")
        print("2.ADMIN SIGN IN")
        print("3.EXIT")

        try:
            choice=int(input("enter the choice: "))
            if choice==1:
                    admin_sign_up()
            elif choice==2:
                admin_sign_in()
            elif choice==3:
                exit_program()
        except ValueError:
             print("Invalid input. Please enter a number.")


def admin_sign_up():
    admin_id=input("enter your admin_id: ")
    while True:
                password = input("\nEnter your new password: ")
    
                if len(password) < 8:
                    print("Password must contain at least 8 characters.")
                elif re.search("[!@#$%&^*]", password) is None:
                    print("Password must have at least 1 special characters.")
                elif re.search("[A-Z]", password) is None:
                    print("Password must have at least 1 capital letter.")
                elif re.search("[a-z]", password) is None:
                    print("Password must have at least 1 lowercase letter.")
                elif re.search("[0-9]", password) is None:
                    print("Password must have at least 1 number.")
                else:
                    print("Valid Password!")

                confirm_password = input("\nRe-enter your password: ")

                if password == confirm_password:
                    admin(admin_id,password)
                    break
        
    
def admin_sign_in():
   while True:
        admin_id = input("enter your admin id: ")
        password= input("enter the password: ")
        mycursor=connection.cursor()
        sql="select * from admin where ADMIN_ID = %s AND PASSWORD = %s"
        users=(admin_id,password)
        mycursor.execute(sql,users)
        result=mycursor.fetchone()
        if result:
           print("sign in sucessfully")
           admin_dashboard()
        else:
            print("invalid details, please try again")


def admin_dashboard():
    while True:
        print("\nWELCOME ")
        print("1.VIEW MOVIES")
        print("2.ADD MOVIES")
        print("3.DELETE MOVIES")
        print("4.VIEW CUSTOMERS DETAILS")
        print("5.BACK")

        try:
            choice=int(input("enter your choice: "))
            if choice==1:
                pass
            elif choice==2:
                add_movies()
            elif choice==3:
                pass
            elif choice==4:
                customers_details()
                break
            elif choice==5:
                pass
            else:
                print("Invalid choice, please try again")
        except ValueError:
            print("Invalid input, please enter the  number")


def customers_details():
    mycursor=connection.cursor()
    sql="select * from customers"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    headers=["ID","NAME","PHONE_NUMBER","PASSWORD"]
    print(tabulate(result,headers=headers,tablefmt="grid"))
    

   
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
            admin_page()
                  
        elif choice == 2:
            customer()

        elif choice == 3:
            exit_program()
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
