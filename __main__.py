import sys

from Admin_domain import *
print("*"*140)
print(f"""@aurthor : Ansh Srivastav
date :{datetime.datetime.now()}""")
print("*"*140)

demo1= User()

while True:
    print()
    print("------------------------------------------------>>> 🙏 Welcome to Shop2Order 🙏 <<<-----------------------------------------------------\n")
    print(demo1.Menu())
    print("+="*25)
    print("1.  For  Create An Account")
    print("2.  For Login ")
    print("0.  For Exit")
    print("+="*25)
    choise = input("Enter Your Choise :")
    if choise == "1":
        print(demo1.signing())
    
    if choise == "2":
        print("--------------->>> Login Domain <<< ----------------\n")
        j = 0
        while j <5:
            email = input("Enter Your Email ID :")
            Password = input("Enter Your Password :")
            ch = demo1.User_login(email,Password)
            if ch == False:                    
                print("            Incorrect Password Try Again             ")
                j+=1
            else:
               
                print()          
                print("              ⭐⭐ Login SucessFully ⭐⭐              ")
                print()
                while True:
                    print()
                    print("=+"*55)
                    print("1 For Search Items")
                    print("2 For Cart ")
                    print("3 For Place an Order ")
                    print("4 For View Order History")
                    print("0 For Exit")
                    print('+='*55)
                    user_choise = input("select an options :")
                    if user_choise == "1":
                        print(demo1.category())
                    
                    if user_choise =="2":
                        print(demo1.carts())
                    
                    if user_choise =="3":
                        print(demo1.order_place())
                    
                    if user_choise =="4":
                        print(demo1.order_history())
                    
                    if user_choise=="0":
                        print()
                        print("    ❤ Thanks For Using Shop2Order  ❤ ")
                        sys.exit()

        print()        
        print("You Have Tried Many Times\n Now you can't login till 30 sec")
        for x in range(30,0,-1):
            second = x%60
            print(f"00:00:{second:02}")
            time.sleep(1)
            print("Now Login Again")
        break

        
    if choise == "0":
        print()
        print("    ❤ Thanks For Using Shop2Order  ❤ ")
        break