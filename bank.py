#------------------------
#Imports
import time





#------------------------
#Functions

def selection():

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

        if user_menu_pick == "1":
            print("1")
            user_menu = True

        elif user_menu_pick == "2":
            print("2")
            user_menu = True

        elif user_menu_pick == "3":
            print("3")
            user_menu = True

        elif user_menu_pick == "4":
            print("4")
            user_menu = True

        elif user_menu_pick == "5":
            print("5")
            user_menu = True
        
        elif user_menu_pick == "6":
            print("6")
            user_menu = True

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
time.sleep(1)
selection()