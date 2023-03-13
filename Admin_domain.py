import json
import time
import datetime
import random

with open("Gerocery.json",'r') as f:
    gecory_temp = json.load(f)

class Admin:
    def __init__(self):
        self.Gecery = {}
            
    def Login(self):
        Login_ID = input("Enter Your Login_ID :")
        if Login_ID =="sriv.ansh":
            i = 1
            while i <5:
                Password = input("Enter Your Password :")
                if Password != "password":
                   
                    print("            Incorrect Password Try Again             ")
                    i+=1
                else:                   
                    print()
                    print( "              ⭐⭐ Login SucessFully ⭐⭐              ")
            print("You Have Tried Many Times\n Now you can't login till 30 sec")
            for x in range(30,0,-1):
                second = x%60
                print(f"00:00:{second:02}")
                time.sleep(1)
           
            return "----------------->>> Now You Can Login Again<<<-----------------"
        else:
           
            return "   ----------->>>>  Enter Valid ID   <<<------------   "


    def Add_grocery(self):
        cat = {}
        items = {}
        key = len(cat)
        cate_name = input("Enter Your Category Name :")
        try:
            nos_items = int(input(f"Enter How Many Category of {cate_name} You Want to Add :"))
        except:
            return "Enter A Valid Number "
        else:
            for j in range(1,nos_items+1):
                item_name = input(f"Enter Your {j} Type of {cate_name} Name  Here :")
                Price = input(f"Enter the Price For {j} {item_name} :")
                Quentity = input(f"Enter Your Quentity for {j} {item_name}:")
                items = {"Item Name":item_name,
                        "Price":Price,"Quentity":Quentity}
                cat[key] = items
                key = len(cat)+1   
            self.Gecery[cate_name] = cat
            with open("Gerocery.json",'w') as f:
                json.dump(self.Gecery,f,indent=4) 
                               
    def View_user(self):
        pass



class User(Admin):
    def __init__(self):
        super().__init__()
        self.persons = {}
        self.cart = []
        global temp
        global gecory_temp
    
    def signing(self):
        print("--------------->>> Signing Domain <<< ----------------\n")
        k = open("User Details.json","r+")
        content = json.load(k)
        name = input("Enter Your Name Here :")
        try : 
            mobile_number = int(input("Enter A Valid Phone Number :"))
        except :
             time.sleep(2)
             print("Enter A Valid Number")
             return ""
        else:
            if len(str(mobile_number)) <10:
                time.sleep(2)
                print( "Number Contain More then 10 Digit")
                return ""
            else:
                email = input("Enter Your Email ID :")
                for i in range(len(content)):
                    if email != content[i]["Email ID"]:
                        password = input("Enter Your Password :")
                        d = {"Name":name,"Mobile Number":mobile_number
                             ,"Email ID":email,"Password":password}
                        content.append(d)
                        k.seek(0)
                        k.truncate()
                        json.dump(content,k,indent=2)
                        print()
                        print("     ✨✨🌟🌟   You Have Registered Sccessfully  ✨✨🌟🌟    ")
                        time.sleep(5)
                    else:
                        print()
                        print("Your Have Already Registered Please Login from login Portal")
                        time.sleep(5)
                    return  ""
            
    def User_login(self,email,password):
        print("--------------->>> Login Domain <<< ----------------\n")
        d = 0
        f = open("User Details.json",'r')
        content = json.load(f)
        for i in range(len(content)):
            if content[i]["Email ID"]==email and content[i]["Password"]==password:
                d=1
                break
        if d ==0:
            return False
        return True

                        


    def Menu(self):
        print("--------------------->>>      Menu's     <<<---------------------------\n")
        j= 1
        print("|--------------------------------------------------------------------- |")
        for i in gecory_temp.keys():
            print("|                                                                      |")
            print(f"|     Items {j}                  |                   {i}                                               ")
            j+=1
        print("|--------------------------------------------------------------------- |")
        return ""


    def category(self):
        items = input("Enter Your Items Name :")
        print("-------------------------------------------->>>>>   Basde On Your Search  <<<<<-------------------------------------- \n")
        print("|----------------------------------------------------------------------------------------------------------- |")
        if items not in  gecory_temp.keys():
            print()
            return "🙁🙁   Sorry Currently It's Unavailable    🙁🙁"
        j = 1
        for i in gecory_temp[items].values():
            print("|                                                                                                             |")
            print(f"| {j}.    {i['Item Name']}          --->>>       {i['Quentity']}       ----->>>                  {i['Price']} ₹    ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            j+=1
        print("|...........................................................................................................|")
        print()
        
        while True:
            print("+="*55)
            print("------>>>>>    Press 0 For Exit ")
            print("------>>>>> Press Any to Add Items in Your Carts ")
            print("+="*55)
            option = input()
            if option == "0":
                break
            else:
                key = input("select item Which You Want to Add :")
                self.cart.append(gecory_temp[items][key])
                print()
                print("    🎆🎆🎊🎊      Congratulation Items Successfully Added to the Cart   🎊🎊🎆🎆      ")
        with open("Order_history.json",'w') as f:
            json.dump(self.cart,f,indent=4)
        print()
        print("🙂🙂  Your Items Got Added Sucessfully  🙂🙂\n🙂🙂  You can Now Check Your Cart  🙂🙂")
        return ""


    def carts(self):
        with open("Order_history.json",'r') as f:
           self.temp =  json.load(f)
        print("-------------------------------------->>> Carts Are <<<-------------------------------\n")
        print(".........................................................................................|")
        for i in self.temp:
            print("|                                                                                          |")
            print(f"       {i}")
        print("|.........................................................................................|")
        return ""

    def order_place(self):
        print("    🎊🎊      You Have Order Sucessfully   🎊🎊        ")
        print()
        temp = datetime.date.today()
        date = temp+ datetime.timedelta(days=5)
        print(f"You Will Get Your Order on {date}....")
        return ""
    
    def order_history(self):
        with open("Order_history.json",'r') as f:
           self.temp =  json.load(f)
        print("---------------->>>  Your Previous Order History is <<<----------------\n")
        for i in self.temp:
            for j , r in i.items(): 
                print("|                                                      |")
                print(f"    {j} --->>       {r}")
        return ""

