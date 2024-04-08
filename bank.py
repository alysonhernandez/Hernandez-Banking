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
            go_back_con == True

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
    
    #old_total = mycursor.execute("SELECT Funds FROM acc_info WHERE Username = %s")
    #acc_val = (user_acc_pick, )
            
    #new_money_total = old_total + money_add
    
    #sql = "SELECT %s UPDATE acc_info SET Funds = %s WHERE Funds = %s"
    #val = (user_acc_pick, new_money_total, old_total, )


    sql = "SELECT SUM(Funds + %s) FROM acc_info WHERE Username = %s"
    val = (money_add, user_acc_pick, )
    mycursor.execute(sql, val)
    
    mydb.commit()

    print("You current funds are:", mycursor, "dollars.")
    print("")
    print("----------------")

    time.sleep(1)
    go_back_menu()


def withdraw_funds():
    print("wip")

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
    user_funds = int(input("                                Funds: "))
    acc_id = int(input("                                ID: "))

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
            
    sql = "DELETE FROM acc_info WHERE Username = %s"
    val = (user_acc_del, )
    mycursor.execute(sql, val)
    mydb.commit()

    print("")
    print("Account has been successfully deleted.")
    print("")
    print("----------------")


    time.sleep(1)
    go_back_menu()



def modify_acc():
    print("wip")

    time.sleep(1)
    go_back_menu()





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