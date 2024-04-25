#------------------------
#Imports
import time
import mysql.connector

#connection = mysql.connector.connect(user = 'root', database = 'hernandez_banking', password = 'r0.#V1a?TH@r$N')
#cursor = connection.cursor()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="r0.#V1a?TH@r$N",
  database="hernandez_banking"
)

mycursor = mydb.cursor()



#------------------------
#Functions

###
### ------------- KEEP AT TOP
###
def go_back_menu():

    go_back_con = False

    while go_back_con == False:
        print("")
        go_back = input("""Would you like to return to the menu? (y/n)
                                > """)
        print("----------------")
        print("")
        
        if go_back.lower() == "y":
            selection()
            go_back_con = True

        elif go_back.lower() == "n":
            go_back_con = True
            print("")
            print("----------------")
            print("Thank you for using our services!")
            print("----------------")
            print("")
            exit()

        else:
            time.sleep(1)
            print("")
            print("--------")
            print("Please choose a valid options. *(y/n)*")
            print("--------")
            print("")
            time.sleep(1)
            go_back_con = False
###
### ------------- KEEP AT TOP
###




def check_balence():

    mycursor.execute("SELECT Username, Funds FROM acc_info")
    myresult = mycursor.fetchall()

    print("----------------")
    print("")
    for item in myresult:
        print("Funds for:", item, "dollars.")
    print("")
    print("--------")

    time.sleep(1)
    go_back_menu()
    


def deposit_funds():
    
    print("----------------")
    print("")

    user_acc_pick = input("""Please type the *USERNAME* of the account to desposit funds into.
                            > """)
    
    
    print("--------")
    print("")
    money_add = int(input("""How much money would you like to deposit?
                            > """))

    
    sql = "SELECT Funds FROM acc_info WHERE Username = %s"
    val = (user_acc_pick, )
    mycursor.execute(sql, val)

    funds_old_result = mycursor.fetchone()

    if funds_old_result:
        funds_old = funds_old_result[0]  
        funds_total = money_add + funds_old 
        sql_2 = "UPDATE acc_info SET Funds = %s WHERE Username = %s"
        val_2 = (funds_total, user_acc_pick)
        mycursor.execute(sql_2, val_2, )
        mydb.commit()

        print("--------")
        print("")
        print("Your current funds are:", funds_total, "dollars.") 
        print("")
        print("--------")

    else:
        print("----------------")
        print("")
        print("User not found.")
        print("")
        print("----------------")


    print("")
    print("----------------")

    time.sleep(1)
    go_back_menu()


def withdraw_funds():
    print("----------------")
    print("")

    user_acc_pick = input("""Please type the *USERNAME* of the account to withdraw funds from.
                            > """)
    
    
    print("--------")
    print("")
    money_sub = int(input("""How much money would you like to withdraw?
                            > """))

    sql = "SELECT Funds FROM acc_info WHERE Username = %s"
    val = (user_acc_pick, )
    mycursor.execute(sql, val)

    funds_old_result = mycursor.fetchone()

    if funds_old_result:
        funds_old = funds_old_result[0]  
        funds_total = funds_old - money_sub

        if funds_total < 0: #if the user puts in a number that is above their funds
            print("----------------")
            print("")
            print("You cannot have a negative balance. Please take out a loan beforehand.")
            print("")
            print("----------------")

            time.sleep(1)
            go_back_menu()

        sql_2 = "UPDATE acc_info SET Funds = %s WHERE Username = %s"
        val_2 = (funds_total, user_acc_pick)
        mycursor.execute(sql_2, val_2, )
        mydb.commit()

        print("--------")
        print("")
        print("Your current funds are:", funds_total, "dollars.") 
        print("")
        print("--------")

    else:
        print("----------------")
        print("")
        print("User not found.")
        print("")
        print("----------------")

    time.sleep(1)
    go_back_menu()




def create_acc():

    print("----------------")
    print("")
    print("Please input the following information.")
    user_full_name = input("                                Full Name: ")
    user_name = input("                                User Name: ")
    user_pass = input("                                Password: ")
    user_Email = input("                                Email: ")
    user_funds_s = input("                                Funds: ")

    while not user_funds_s.isdigit():
        print("--------")
        print("")
        print("Invalid number. Please input *only digits*")
        print("")
        print("--------")
        print("")
        user_funds_s = input("                                Funds: ")

    user_funds = int(user_funds_s)

    acc_id_s = input("                                ID: ")

    while not acc_id_s.isdigit():
        print("--------")
        print("")
        print("Invalid number. Please input *only digits*")
        print("")
        print("--------")
        print("")
        acc_id_s = input("                                ID: ")

    acc_id = int(acc_id_s)



    sql = "INSERT INTO acc_info(ID, Full_Name, Username, Password, Email, Funds) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (acc_id, user_full_name, user_name, user_pass, user_Email, user_funds)
    mycursor.execute(sql, val)

    mydb.commit()

    print("")
    print("New account has been successfully added.")
    print("")
    print("----------------")

    time.sleep(1)
    go_back_menu()


def delete_acc():

    print("----------------")
    print("")

    user_acc_del = (input("""Please type the *USERNAME* of the account to be deleted.
                        > """))
    
    sql = "SELECT Username FROM acc_info WHERE Username = %s"
    val = (user_acc_del, )
    mycursor.execute(sql, val)

    username_result = mycursor.fetchone()

    if username_result:

        print("")
        time.sleep(1)
        #confirms account deletion with a password
        user_del_con = input("""Enter the *PASSWORD** of the account to continue deletion.
                        > """)
        
        sql_2 = "SELECT Password FROM acc_info WHERE Username = %s"
        val_2 = (user_acc_del, )
        mycursor.execute(sql_2, val_2)
        password_result = mycursor.fetchone()

    
        if password_result and password_result[0] == user_del_con:
            sql_3 = "DELETE FROM acc_info WHERE Username = %s"
            val_3 = (user_acc_del, )
            mycursor.execute(sql_3, val_3)
            mydb.commit()

            print("")
            print("Account has been successfully deleted.")
            print("")
            print("----------------")


        else:
            print("----------------")
            print("")
            print("Password does not match.")
            print("")
            print("----------------")

    else:
        print("----------------")
        print("")
        print("User not found.")
        print("")
        print("----------------")




    time.sleep(1)
    go_back_menu()



def modify_acc():
    
    print("----------------")
    print("")
    
    print("Edit Account Information:.")
    print("""
    - Full Name
    - Username
    - Password
    - Email
    - None (Go back to menu)
          """)
    
    user_menu = False

    while user_menu == False:
        time.sleep(1)
        user_modify_pick = input("""Please choose one of the options to continue.
                                > """)

        if user_modify_pick.lower() == "full name":
            time.sleep(1)

            user_acc_mod = (input("""Please type the *USERNAME* of the account to be modifed.
                                    > """))
            print("")
            time.sleep(1)

            user_new_name = (input("""Please type the *FULL NAME* you would like to change to.
                                    > """))
            
            sql = "UPDATE acc_info SET Username = %s WHERE Username = %s"
            val = (user_new_name, user_acc_mod, )
            mycursor.execute(sql, val)

            print("")
            print("Full Name has been successfully changed.")
            print("")
            print("----------------")






            






            
            user_menu = True


        #Deposits user's money into account
        elif user_modify_pick.lower() == "username":
            time.sleep(1)
            deposit_funds()
            user_menu = True

        #Withdraws user's money into account
        elif user_modify_pick.lower() == "password":
            time.sleep(1)
            withdraw_funds()
            user_menu = True

        #Makes a new account
        elif user_modify_pick.lower() == "email":

            time.sleep(1)
            create_acc()
            user_menu = True

        #Removes an account
        elif user_modify_pick.lower() == "none":
            time.sleep(1)
            go_back_menu()
            user_menu = True

        else:
            print("")
            print("--------")
            print("Please choose a valid options.")
            print("--------")
            print("")
            user_menu = False
    






def selection():

    time.sleep(1)

    #Lists out the options for the user
    print("Here is how we can help you today.")
    print("""
    1. Check Account Balance
    2. Desposit Funds
    3. Withdraw Funds
    4. Create a New Account
    5. Delete An Account
    6. Modify Account Details
    0. Exit Program

          """)
    
    user_menu = False

    while user_menu == False:
        #Lets the user choose how they want to continue
        time.sleep(1)
        user_menu_pick = input("""Please choose one of the options to continue.
                                > """)

        #Checks user's balance
        if user_menu_pick == "1":
            time.sleep(1)
            check_balence()
            user_menu = True


        #Deposits user's money into account
        elif user_menu_pick == "2":
            time.sleep(1)
            deposit_funds()
            user_menu = True

        #Withdraws user's money into account
        elif user_menu_pick == "3":
            time.sleep(1)
            withdraw_funds()
            user_menu = True

        #Makes a new account
        elif user_menu_pick == "4":

            time.sleep(1)
            create_acc()
            user_menu = True

        #Removes an account
        elif user_menu_pick == "5":
            time.sleep(1)
            delete_acc()
            user_menu = True

        #Modify's account details
        elif user_menu_pick == "6":
            time.sleep(1)
            modify_acc()
            user_menu = True

        #Exits program
        elif user_menu_pick == "0":
            user_menu = True
            print("")
            print("----------------")
            print("Thank you for using our services!")
            print("----------------")
            print("")
            exit()

        else:
            print("")
            print("--------")
            print("Please choose a valid options. (0-6)")
            print("--------")
            print("")
            user_menu = False






#------------------------
#Greeting

print("")
print("----------------")
print("Welcome to the Hernandez Banking Help Center!")
print("----------------")
print("")
selection()