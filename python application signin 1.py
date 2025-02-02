import pymysql

def signup_db(email, password):
    signup = False
    try:

        mydb=None
        myCursor=None

        mydb = pymysql.connect(host="localhost", user="urwa", password="urwatulwusqa", database="ecommercesitee")
        query = "INSERT INTO users (email, password) VALUES (%s, %s);"
        args = (email, password)
        mycursor = mydb.cursor()
        mycursor.execute(query, args)
        mydb.commit()
        signup = True
    except Exception as e:
        print(str(e))
    finally:
        if mycursor!=None:
            mycursor.close()
        if mydb!=None:
            mydb.close()
        return signup

def signin_db(email, password):
    signin = False
    try:

        mydb=None
        myCursor=None

        mydb = pymysql.connect(host="localhost", user="urwa", password="urwatulwusqa", database="ecommercesite")
        query = "SELECT email, password FROM users WHERE email=%s AND password=%s;"
        args = (email, password)
        mycursor = mydb.cursor()
        mycursor.execute(query, args)
        row = mycursor.fetchone()
        if row!=None:
            signin = True

    except Exception as e:
        print(str(e))
    finally:
        if mycursor!=None:
            mycursor.close()
        if mydb!=None:
            mydb.close()
        return signin

def displayAll():
    signin=False
    try:

        mydb=None
        myCursor=None

        mydb = pymysql.connect(host="localhost", user="urwa", password="urwatulwusqa", database="ecommercesite")
        query = "SELECT email, password FROM users"
        mycursor = mydb.cursor()
        mycursor.execute(query)
        rows = mycursor.fetchall()
        for r in rows:
            print(f"Email:", r[0], "Password:", r[1])
    except Exception as e:
        print(str(e))
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

def signinview():
    email = input("Enter email to sign in: ")
    password = input("Enter password: ")
    signin = signin_db(email, password)
    if signin:
        print("Login successful")
    else:
        print("Login failed")

def signupview():
    email = input("Enter email to sign up: ")
    password = input("Enter password: ")
    signup = signup_db(email, password)
    if signup:
        print("Signup successful")
    else:
        print("Signup failed")

def main():
    print('Welcome to the E-commerce System')
    sentinel = True
    while sentinel:
        print("\nPlease choose an option:")
        print("1 - Sign In")
        print("2 - Sign Up")
        print("3 - Display All Records")
        print("0 - Quit App")
        option = input("Please choose your option: ")
        try:
            option = int(option)
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if option == 1:
            signinview()
        elif option == 2:
            signupview()
        elif option == 3:
            displayAll()
        elif option == 0:
            sentinel = False
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
