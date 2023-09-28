import tkinter as tk
from tkinter import Frame, Label, Toplevel, Entry, Button, messagebox
from PIL import Image, ImageTk
from colorama import  Fore, Back, Style
from colorama import  Fore, Back, Style
from playsound import playsound
from tkinter.ttk import Button
 

global guiInput
labellist = []
newlist = []

class Money:
    def __init__(self, dollars, quarters, dimes, nickels, pennies):
        self.dollars = dollars
        self.quarters = quarters
        self.dimes = dimes
        self.nickels = nickels
        self.pennies = pennies
    def get_info(self):
        return self.dollars, self.quarters, self.dimes, self.nickels, self.pennies
    def printMoney(self):
        print(self.get_info())

class myInventory:
    def __init__(self):
        self.current_inv = []
        self.num_items = 0
        pass
    def addInv(self, item):
        self.current_inv.append(item)
        self.num_items += 1
    def get_info(self, i):
        return self.current_inv[i].ID, self.current_inv[i].name, self.current_inv[i].quantity, self.current_inv[i].price
    def printInv(self):
        print(Fore.BLUE + Style.BRIGHT + "\nInventory:\nID  Item  Quantity  Price" + Style.RESET_ALL + Fore.BLUE)
        label1 = Label(window, text = "\nInventory\nID  Item  Quantity  Price")
        label1.place(x=40,y=90)
        labellist.append(label1)
        #label.after(5000, label.config(text=''))
        for i in range(0, self.num_items):
            print(self.get_info(i))
            label2 = Label(window, text = self.get_info(i))
            label2.place(x=60,y=140+(i*20))
            labellist.append(label2)
        print(Style.RESET_ALL)
    def find(self, compare, price, iteration):
        for i in range(0, self.num_items):
            if self.current_inv[i].name == compare:
                price = self.current_inv[i].price
                iteration = i
                break
        return price, iteration
    def sellItem(self, value):
        self.current_inv[value].quantity = self.current_inv[value].quantity - 1

class myItem:
    def __init__(self, ID, name, quantity, price):
        self.ID = ID
        self.name = name
        self.quantity = quantity
        self.price = price

    def get_info(self):
        return f"{self.ID}, {self.name}, {self.quantity}, ${self.price}"
    
    def deleteItem(self):
        del(self.ID)

def calcChange(change):
    while change >= 1:
        properChange.dollars += 1
        vendingMoney.dollars -= 1
        change -= 1
    while change >= .25:
        properChange.quarters += 1 
        vendingMoney.quarters -= 1
        change -= .25
    while change >= .10:
        properChange.dimes += 1 
        vendingMoney.dimes -= 1
        change -= .10
    while change >= .05:
        properChange.nickels += 1
        vendingMoney.nickels -= 1 
        change -= .05
    while change >= .01:
        properChange.pennies += 1
        vendingMoney.pennies -= 1
        change -= .01
    return change
        
def calcPrice(price, twoWords, userInput):

    if twoWords == 0:
        myMoney = Money(int(userInput[3]), int(userInput[4]), int(userInput[5]), int(userInput[6]), int(userInput[7]))
        myCash = int(userInput[3]) + int(userInput[4])*.25 + int(userInput[5])*.10 + int(userInput[6])*.05 + int(userInput[7])*.01 
    else: 
        myMoney = Money(int(userInput[4]), int(userInput[5]), int(userInput[6]), int(userInput[7]), int(userInput[8]))
        myCash = int(userInput[4]) + int(userInput[5])*.25 + int(userInput[6])*.10 + int(userInput[7])*.05 + int(userInput[8])*.01 
    
    change = myCash - price
    vendingChange = (vendingMoney.dollars + vendingMoney.quarters*.25 + vendingMoney.dimes*.10 + vendingMoney.nickels*.05 + vendingMoney.pennies*.01)
    
    if change < 0:
        return -1
    elif change > vendingChange:
        return -2
    else:
        vendingMoney.dollars += myMoney.dollars        
        vendingMoney.quarters += myMoney.quarters
        vendingMoney.dimes += myMoney.dimes
        vendingMoney.nickels += myMoney.nickels
        vendingMoney.pennies += myMoney.pennies
        calcChange(change)
        return change

def printSomething(var):
    if var == 0:
        label = Label(window, text = "Item already exists. Please input something differerent", font =('Helvetica 13'), fg="red")
        label.place(x=150,y=0)
        label.after(2000, lambda: label.config(text=''))
        print(Fore.BLUE + "\nItem already exists. Please add something different\n" + Style.RESET_ALL)
    elif var == 1:
        label = Label(window, text = "Item successfully added", fg='blue', font =('Helvetica 13'))
        label.place(x=250, y=0)
        label.after(2000, lambda: label.config(text=''))
        print(Fore.BLUE + "\nItem successfully added\n" + Style.RESET_ALL)
    elif var == 2:
        label = Label(window, text = "Please follow the guidelines in *help* when making your request", font =('Helvetica 13'))
        label.place(x=120, y=0)
        label.after(2000, lambda: label.config(text=''))
        print(Fore.RED + "\nPlease follow the guidelines in *help* when making your request\n" + Style.RESET_ALL)
    elif var == 3:
        print(Fore.RED + "\nImproper Input Format\n" + Style.RESET_ALL)
        label = Label(window, text = "\nImproper Input Format", fg='red', font =('Helvetica 13'))
        label.place(x=250, y=-20)
        label.after(2000, lambda: label.config(text=''))
    elif var == 4:
        print(Fore.RED + "\nError! Request not recognized\n" + Style.RESET_ALL)
        label = Label(window, text = "Error! Request not recognized", fg= 'red', font =('Helvetica 13'))
        label.place(x=230, y=0)
        label.after(2000, lambda: label.config(text=''))
    elif var == 5:
        label = Label(window, text = "\nTo navigate the vending machine, please use one of the following commands:\n\n[add item name quantity $price]\t Adds an item to the vending machine if it does not already exist. Must use '$'\n[balance]\t\t\t\t Shows the current balance of the vending machine\n[buy item name #dollars #quarters #dimes #nickels #pennies] Buys an item from the vending machine. NOTE: Zeros must be inputted for any currency not used\n[exit]\t\t\t\t Exits the vending machine\n[help]\t\t\t\t Displays the help table\n[history]\t\t\t\t Shows the previous requested transactions\n[inventory]\t\t\t Shows the current inventory of the vending machine\n", font =('Helvetica 10'), justify='left', wraplength=600, bg='lightgrey', fg='red')
        label.place(x = 50, y = 155)
        label.after(5000, lambda:label.config(text=""))
        history.append(newlist)
    elif var == 6:
        print(Fore.RED + "\nYou do not have the appropriate funds to purchase this item\n" + Style.RESET_ALL)
        label = Label(window, text = "You do not have the appropriate funds to purchase this item", fg= 'red', font =('Helvetica 13'))
        label.place(x=125, y=0)
        label.after(2000, lambda: label.config(text=''))
    elif var == 6:
        print(Fore.RED + "\nItem not found\n" + Style.RESET_ALL)
        label = Label(window, text = "Item not found", fg="red")
        label.place(x=250,y=0)
        label.after(3000, lambda:label.config(text=""))
    else:
        return;

def addItemFunc(userInput, priceInput):
#for i in range(0,len(myInventory)):
    if userInput[2].isdigit() or len(userInput) > 9:
        return -1
    elif userInput[3].isdigit():
        findItem = vending.find(userInput[2], 0, -1) #inputs a price of $0 and array value of -1
        price = findItem[0]
        arrayValue = findItem[1]
        if price != 0:
           printSomething(0)
        else:
            newItem = myItem(vending.num_items + 1, userInput[2], int(userInput[3]), float(priceInput[1]))
            vending.addInv(newItem)
            printSomething(1)
    else: 
        findItem = vending.find(userInput[2]+' '+userInput[3], 0, -1) #inputs a price of $0 and array value of -1
        price = findItem[0]
        arrayValue = findItem[1]
        if price != 0:
            printSomething(0)
        else:
            newItem = myItem(vending.num_items + 1, userInput[2]+' '+userInput[3], int(userInput[4]), float(priceInput[1]))
            vending.addInv(newItem)
            printSomething(1)
    return 0

def buyItemFunc(userInput):
    if userInput[2].isdigit() or len(userInput) > 9:
        return -1
    elif userInput[3].isdigit():
        twoWords = 0
        findItem = vending.find(userInput[2], 0, -1) #inputs a price of $0 and array value of -1
        price = findItem[0]
        arrayValue = findItem[1]
        if price!= 0:  #theoretically if the price != $0 then the item was found and the array value is returned
            checkFunds = calcPrice(price, twoWords, userInput)
            if checkFunds == -1:
                printSomething(6)
            elif checkFunds == -2:
                print(Fore.RED + "\nIm sorry, this vending machine does not have enough change to properly reimburse you. The max amount of change this machine can give you is", Style.BRIGHT + "${:,.2f}".format(vendingMoney.dollars + vendingMoney.quarters*.25 + vendingMoney.dimes*.10 + vendingMoney.nickels*.05 + vendingMoney.pennies*.01), "\n" + Style.RESET_ALL)
                label = Label(window, fg="red", text = "Im sorry, this vending machine does not have enough change to properly reimburse you.\nThe max amount of change this machine can give you is ${:,.2f}".format(vendingMoney.dollars + vendingMoney.quarters*.25 + vendingMoney.dimes*.10 + vendingMoney.nickels*.05 + vendingMoney.pennies*.01))
                label.place(x=100,y=0)
                label.after(3000, lambda:label.config(text=""))
            else: 
                vending.sellItem(arrayValue)
                print(Fore.BLUE + "\nYou have successfully purchased", userInput[2])
                print(Fore.BLUE + "Your change is:", "${:,.2f}".format(properChange.dollars + properChange.quarters*.25 + properChange.dimes*.10 + properChange.nickels*.05 + properChange.pennies*.01))
                label = Label(window, text= "You have successfully purchased %s\nYour change is: ${:,.2f}".format(properChange.dollars + properChange.quarters*.25 + properChange.dimes*.10 + properChange.nickels*.05 + properChange.pennies*.01) % userInput[2], fg="green")
                label.place(x=230, y=0)
                label.after(3000, lambda:label.config(text=""))
                print(Style.RESET_ALL)
    elif userInput[4].isdigit(): 
        twoWords = 1
        findItem = vending.find(userInput[2]+' '+userInput[3], 0, -1) #inputs a price of $0 and array value of -1
        price = findItem[0]
        arrayValue = findItem[1]
        if price!= 0:  #theoretically if the price != $0 then the item was found and the array value is returned
            checkFunds = calcPrice(price, twoWords, userInput)
            if checkFunds == -1:
                printSomething(6)
            elif checkFunds == -2:
                label = Label(window, fg= "red", text = "Im sorry, this vending machine does not have enough change to properly reimburse you.\nThe max amount of change this machine can give you is ${:,.2f}".format(vendingMoney.dollars + vendingMoney.quarters*.25 + vendingMoney.dimes*.10 + vendingMoney.nickels*.05 + vendingMoney.pennies*.01))
                label.place(x=100,y=0)
                label.after(3000, lambda:label.config(text=""))
            else: 
                vending.sellItem(arrayValue)
                print(Fore.BLUE + "\nYou have successfully purchased", userInput[2]+' '+userInput[3])
                print(Fore.BLUE + "Your change is:", "${:,.2f}".format(properChange.dollars + properChange.quarters*.25 + properChange.dimes*.10 + properChange.nickels*.05 + properChange.pennies*.01))
                label = Label(window, text= "You have successfully purchased %s\nYour change is: ${:,.2f}".format(properChange.dollars + properChange.quarters*.25 + properChange.dimes*.10 + properChange.nickels*.05 + properChange.pennies*.01) % (userInput[2]+' '+userInput[3]), fg="green")
                label.place(x=230, y=0)
                label.after(3000, lambda:label.config(text=""))
                print(Style.RESET_ALL)
    else:
        printSomething(7)
    return 0

#Create our vending machine
myBalance = 40
history = []
properChange = Money(0, 0, 0, 0, 0)
vending = myInventory()

chips = myItem(1, "chips", 10, 3.50)
vending.addInv(chips)
soda = myItem(2, "coke", 11, 4.25)
vending.addInv(soda)
airpods = myItem(3, "airpods", 3, 60.00)
vending.addInv(airpods)
plush = myItem(4, "plushie", 14, 15.25)
vending.addInv(plush)
kitkat = myItem(5, "kitkat", 11, 3.50)
vending.addInv(kitkat)
gum = myItem(6, "gum", 15, 4)
vending.addInv(gum)

vendingMoney = Money(19, 30, 21, 20, 40)
theInput = [50]
#Welcome message
print(Fore.BLACK + Style.DIM + "\n======================================\n++++++++++++++++++++++++++++++++++++++\n======================================" + Style.RESET_ALL)
print(Fore.BLUE + Style.BRIGHT + "WELCOME TO THE ULTIMATE VENDING MACHINE"+ Style.RESET_ALL, end="")
print(Fore.BLACK + Style.DIM + "\n======================================\n++++++++++++++++++++++++++++++++++++++\n======================================\n"+ Style.RESET_ALL)


def handle_click():
    theInput = entry.get()
    if len(theInput) > 40 or len(theInput) == 0:
        printSomething(2)
    else:
        userInput = theInput.split()
        history.append(theInput)
        priceInput = theInput.split("$")

        #compare userinput to known commands
        if userInput[0] == 'add' and len(userInput) > 1:
            if userInput[1] == 'item':
                if len(priceInput) > 1:
                    inputCheck = addItemFunc(userInput, priceInput)
                    if inputCheck == -1:
                        printSomething(3)
                else:
                    printSomething(3)
            else:
                printSomething(4)
        elif userInput[0] == 'buy' and len(userInput) > 1:
            if userInput[1] == 'item':
                inputCheck = buyItemFunc(userInput)
            else: 
                printSomething(4)
            if inputCheck == -1:
                printSomething(3)         
        elif userInput[0] == 'balance':
            label = Label(window, text ="Vending Machine Currency\n %s dollars\n %s quarters\n %s dimes\n %s nickels\n %s pennies\n The total balance is: ${:,.2f}".format(vendingMoney.dollars + vendingMoney.quarters*.25 + vendingMoney.dimes*.10 + vendingMoney.nickels*.05 + vendingMoney.pennies*.01) % (vendingMoney.dollars, vendingMoney.quarters, vendingMoney.dimes, vendingMoney.nickels, vendingMoney.pennies))
            label.place(x=40,y=60)
            label.after(5000, lambda:label.config(text=""))
            print(Fore.GREEN + "\nThe current currency of the vending machine is as follows:" + Style.RESET_ALL)
            print(Fore.GREEN + "", vendingMoney.dollars, Fore.BLACK + "dollars", Fore.GREEN + "", vendingMoney.quarters, Fore.BLACK + "quarters", Fore.GREEN + "", vendingMoney.dimes, Fore.BLACK + "dimes", Fore.GREEN + "", vendingMoney.nickels, Fore.BLACK + "nickels", Fore.GREEN + "", vendingMoney.pennies, Fore.BLACK + "pennies")
            print(Fore.GREEN + "The total balance of the vending machine is:", Style.BRIGHT + "${:,.2f}".format(vendingMoney.dollars + vendingMoney.quarters*.25 + vendingMoney.dimes*.10 + vendingMoney.nickels*.05 + vendingMoney.pennies*.01), "\n" + Style.RESET_ALL)
        elif userInput[0] == 'inventory':
            vending.printInv()  
        elif userInput[0] == 'history':
            print(Fore.YELLOW + Style.BRIGHT + "\nThe following transactions have been requested:" + Style.RESET_ALL + Fore.YELLOW)
            label = Label(window, text = "Requested Transactions")
            label.place(x=20,y=50)
            labellist.append(label)
            for i in range(0, len(history)):
                print(i+1, history[i])
                #variable = tk.StringVar(history[i])
                label = Label(window, text = "%s:" % (i+1))
                label.place(x=20,y=70+(i*20))
                labellist.append(label)
                label = Label(window, text = "%s" % history[i])
                label.place(x=35,y=70+(i*20))
                labellist.append(label)
            print(Style.RESET_ALL)
        elif userInput[0] == 'help':
            printSomething(5)
            print(Fore.RED + Style.BRIGHT + "\nTo navigate the vending machine, please use one of the following commands:" + Style.RESET_ALL)
            print(Fore.RED + "[add item name quantity $price]\t\t", Fore.LIGHTRED_EX + "Adds an item to the vending machine if it does not already exist. Must use '$'" + Style.RESET_ALL)
            print(Fore.RED + "[balance]\t\t\t\t", Fore.LIGHTRED_EX + "Shows the current balance of the vending machine" + Style.RESET_ALL)
            print(Fore.RED + "[buy item name #dollars #quarters #dimes #nickels #pennies]", Fore.LIGHTRED_EX + "Buys an item from the vending machine. NOTE: Zeros must be inputted for any currency not used" + Style.RESET_ALL)
            print(Fore.RED + "[exit]\t\t\t\t\t", Fore.LIGHTRED_EX + "Exits the vending machine" + Style.RESET_ALL)
            print(Fore.RED + "[help]\t\t\t\t\t", Fore.LIGHTRED_EX + "Displays the help table" + Style.RESET_ALL)
            print(Fore.RED + "[history]\t\t\t\t", Fore.LIGHTRED_EX + "Shows the previous requested transactions" + Style.RESET_ALL)
            print(Fore.RED + "[inventory]\t\t\t\t", Fore.LIGHTRED_EX + "Shows the current inventory of the vending machine\n" + Style.RESET_ALL)
        elif userInput[0] == 'exit':
            print(Fore.BLACK + Style.DIM + "\n=====================================================================\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n=====================================================================" + Style.RESET_ALL)
            print(Fore.BLUE + Style.BRIGHT + "THANK YOU FOR VISITING THE ULTIMATE VENDING MACHINE. HAVE A GOOD DAY"+ Style.RESET_ALL, end="")
            print(Fore.BLACK + Style.DIM + "\n=====================================================================\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n====================================================================="+ Style.RESET_ALL)
            playsound("Mario Death - QuickSounds.com.mp3")
            window.destroy()
        else:
            printSomething(4)
        properChange.dollars = 0
        properChange.quarters = 0
        properChange.dimes = 0
        properChange.nickels = 0
        properChange.pennies = 0
        inputCheck = 0
        twoWords = -1

def item_button_click(item):
    newlist.append("buy")
    newlist.append("item")
    newlist.append(item)
    def calculate_total():
        try:
            dollars = int(dollar_entry.get())
            newlist.append(str(dollars))
            quarters = int(quarter_entry.get())
            newlist.append(str(quarters))
            dimes = int(dime_entry.get())
            newlist.append(str(dimes))
            nickels = int(nickel_entry.get())
            newlist.append(str(nickels))
            pennies = int(penny_entry.get())
            newlist.append(str(pennies))

            total = dollars + (quarters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies*0.01)
            inputCheck = buyItemFunc(newlist)
            if inputCheck == -1:
                printSomething(3)
            properChange.dollars = 0
            properChange.quarters = 0
            properChange.dimes = 0
            properChange.nickels = 0
            properChange.pennies = 0
            inputCheck = 0
            twoWords = -1
            history.append(newlist)

            ''' if total >= 2.50:  # Set this to the cost of a coke
                messagebox.showinfo("Success", "Enjoy your coke!")
                top.destroy()
            else:
                messagebox.showwarning("Insufficient Funds", "You don't have enough money.")'''
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid coin counts.")
        finally:
            top.destroy()
    
    top = Toplevel(window)
    top.title("Payment")

    Label(top, text="Enter your coins:").pack(pady=10)

    dollar_entry = Entry(top, width=10)
    dollar_entry.pack(pady=5)
    Label(top, text="Dollars").pack()

    quarter_entry = Entry(top, width=10)
    quarter_entry.pack(pady=5)
    Label(top, text="Quarters").pack()

    dime_entry = Entry(top, width=10)
    dime_entry.pack(pady=5)
    Label(top, text="Dimes").pack()

    nickel_entry = Entry(top, width=10)
    nickel_entry.pack(pady=5)
    Label(top, text="Nickels").pack()

    penny_entry = Entry(top, width=10)
    penny_entry.pack(pady=5)
    Label(top, text="Pennies").pack()

    Button(top, text="Submit", command=calculate_total).pack(pady=20)

window = tk.Tk()
##size of main window
window.geometry("700x600")
frame = Frame(window, width=800, height=800)
frame.place(anchor='center',relx=0.5, rely=0.5)

img = Image.open("vendingnew.png")
##size of particular image
resize_image = img.resize((500, 700))
newImg = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image

#window.attributes('-alpha',0.5)

label = tk.Label(frame, 
                 text="Hello, Tkinter", 
                 #background="white",
                 ##size of our working canvas
                 width = 1000,
                 height = 800,
                 image = newImg)
##adds the greeting to our window

def remove_data():
    for label in labellist:
        label["text"] = ""
    newlist.clear()

def addInvProperly():
    history.append("inventory")
    vending.printInv()
        
def get_data():
   label.config(text= entry.get(), font= ('Helvetica 13'))

#Create an Entry Widget
entry = tk.Entry(window, width= 42)
entry.place(relx= .47, rely= .87, anchor= "center")
#entry.delete(0, 'end')

#Inititalize a Label widget
label2= tk.Label(window, text="", font=('Helvetica 13'))
frame.pack()
label.pack()
label2.pack()

#Create a Button to get the input data
button = tk.Button(window, text= "Enter Request", width = 20, height = 3, bg='grey', command=handle_click).place(relx= .45, rely= .79, anchor= "center")

itemImg = Image.open("Finished\coca-cola-591ml-04904403.png")
resize_image = itemImg.resize((50, 40))
cokeImg = ImageTk.PhotoImage(resize_image)

button = tk.Button(window, image=cokeImg, width=40, height=45, borderwidth=0, command=lambda:item_button_click("coke"), bg='black', activebackground='white', highlightthickness=0).place(relx= .35, rely= .12, anchor= "center")

chipImg = Image.open("bagochips1.png")
resize_image = chipImg.resize((50, 40))
chipImg = ImageTk.PhotoImage(resize_image)

button = tk.Button(window, image=chipImg, width=40, height=45, borderwidth=0, command=lambda:item_button_click("chips"), bg='black', activebackground='white', highlightthickness=0).place(relx= .45, rely= .12, anchor= "center")

cocoaImg = Image.open("Finished/chocolate1.png")
resize_image = cocoaImg.resize((50, 60))
cocoaImg= ImageTk.PhotoImage(resize_image)

button = tk.Button(window, image=cocoaImg, width=40, height=30, borderwidth=0, command=lambda:item_button_click("kitkat"), bg='black', activebackground='white', highlightthickness=0).place(relx= .485, rely= .37, anchor= "center")

gumImg = Image.open("Finished/gum2.png")
resize_image = gumImg.resize((50, 40))
gumImg= ImageTk.PhotoImage(resize_image)

button = tk.Button(window, image=gumImg, width=35, height=25, borderwidth=0, command=lambda:item_button_click("gum"), bg='black', activebackground='white', highlightthickness=0).place(relx= .41, rely= .49, anchor= "center")

kirbyImg = Image.open("Finished/kribydone.png")
resize_image = kirbyImg.resize((55, 55))
kirbyImg= ImageTk.PhotoImage(resize_image)

button = tk.Button(window, image=kirbyImg, width=50, height=48, borderwidth=0, command=lambda:item_button_click("plushie"), bg='black', activebackground='white', highlightthickness=0).place(relx= .45, rely= .59, anchor= "center")

aImg = Image.open("Finished/airpodsdoneoutofframe.png")
resize_image = aImg.resize((30, 30))
aImg= ImageTk.PhotoImage(resize_image)

button = tk.Button(window, image=aImg, width=26, height=30, borderwidth=0, command=lambda:item_button_click("airpods"), bg='black', activebackground='black', highlightthickness=0).place(relx= .59, rely= .25, anchor= "center")

button = tk.Button(window, text= "Inventory", command= lambda:addInvProperly(), bg ='grey', highlightthickness=0).place(relx= .45, rely= .67, anchor= "center")

myImg = Image.open("question.png")
resize_image = myImg.resize((30, 30))
click_btn = ImageTk.PhotoImage(resize_image)

button = tk.Button(window, image=click_btn, command= lambda:printSomething(5), width=30, height=30, borderwidth=0).place(relx= .95, rely= .05, anchor= "center")
#button.bind("<Button-1>", handle_click)

button = tk.Button(window, text= "Clear", command= remove_data, bg ='grey', height = 1).place(relx= .69, rely= .87, anchor= "center")
##runs out previous window applications
window.mainloop()

