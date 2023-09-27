import tkinter as tk
from tkinter import Frame, ttk, Label
from PIL import Image, ImageTk
from colorama import  Fore, Back, Style
from colorama import  Fore, Back, Style

global guiInput

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
        print(Fore.BLUE + Style.BRIGHT + "\nThe vending machine consists of the following options:\nID  Item  Quantity  Price" + Style.RESET_ALL + Fore.BLUE)
        label = Label(window, text = "\nThe vending machine consists of the following options:\nID  Item  Quantity  Price")
        for i in range(0, self.num_items):
            print(self.get_info(i))
            Label(window, text = self.get_info(i))
            label.place(x=40+(i+5),y=90)
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
        label = Label(window, text = "Item already exists. Please input something differerent", font =('Helvetica 13'))
        label.place(x=40,y=90)
        print(Fore.BLUE + "\nItem already exists. Please add something different\n" + Style.RESET_ALL)
    elif var == 1:
        label = Label(window, text = "\nItem already exists. Please add something different\n", font =('Helvetica 13'))
        label.pack()
    elif var == 2:
        label = Label(window, text = "Item successfully added.", font =('Helvetica 13'))
        label.pack()
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
            printSomething(2)
    else: 
        findItem = vending.find(userInput[2]+' '+userInput[3], 0, -1) #inputs a price of $0 and array value of -1
        price = findItem[0]
        arrayValue = findItem[1]
        if price != 0:
            printSomething(1)
        else:
            newItem = myItem(vending.num_items + 1, userInput[2]+' '+userInput[3], int(userInput[4]), float(priceInput[1]))
            vending.addInv(newItem)
            printSomething(2)
    return 0

def buyItemFunc(userInput, priceInput):
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
                print(Fore.RED + "\nYou do not have the appropriate funds to purchase this item\n" + Style.RESET_ALL)
            elif checkFunds == -2:
                print(Fore.RED + "\nIm sorry, this vending machine does not have enough change to properly reimburse you. The max amount of change this machine can give you is", Style.BRIGHT + "${:,.2f}".format(vendingMoney.dollars + vendingMoney.quarters*.25 + vendingMoney.dimes*.10 + vendingMoney.nickels*.05 + vendingMoney.pennies*.01), "\n" + Style.RESET_ALL)
            else: 
                vending.sellItem(arrayValue)
                print(Fore.BLUE + "\nYou have successfully purchased", userInput[2])
                print(Fore.BLUE + "Your change is:", "${:,.2f}".format(properChange.dollars + properChange.quarters*.25 + properChange.dimes*.10 + properChange.nickels*.05 + properChange.pennies*.01))
                print(Style.RESET_ALL)
    elif userInput[4].isdigit(): 
        twoWords = 1
        findItem = vending.find(userInput[2]+' '+userInput[3], 0, -1) #inputs a price of $0 and array value of -1
        price = findItem[0]
        arrayValue = findItem[1]
        if price!= 0:  #theoretically if the price != $0 then the item was found and the array value is returned
            checkFunds = calcPrice(price, twoWords, userInput)
            if checkFunds == -1:
                print(Fore.RED + "\nYou do not have the appropriate funds to purchase this item\n" + Style.RESET_ALL)
            elif checkFunds == -2:
                print(Fore.RED + "\nIm sorry, this vending machine does not have enough change to properly reimburse you. The max amount of change this machine can give you is", Style.BRIGHT + "${:,.2f}".format(vendingMoney.dollars + vendingMoney.quarters*.25 + vendingMoney.dimes*.10 + vendingMoney.nickels*.05 + vendingMoney.pennies*.01), "\n" + Style.RESET_ALL)
            else: 
                vending.sellItem(arrayValue)
                print(Fore.BLUE + "\nYou have successfully purchased", userInput[2]+' '+userInput[3])
                print(Fore.BLUE + "Your change is:", "${:,.2f}".format(properChange.dollars + properChange.quarters*.25 + properChange.dimes*.10 + properChange.nickels*.05 + properChange.pennies*.01))
                print(Style.RESET_ALL)
    else:
        print(Fore.RED + "\nItem not found\n" + Style.RESET_ALL)
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
oreos = myItem(5, "oreos", 11, 3.50)
vending.addInv(oreos)

vendingMoney = Money(19, 30, 21, 20, 40)
theInput = [50]

#Welcome message
print(Fore.BLACK + Style.DIM + "\n======================================\n++++++++++++++++++++++++++++++++++++++\n======================================" + Style.RESET_ALL)
print(Fore.BLUE + Style.BRIGHT + "WELCOME TO THE ULTIMATE VENDING MACHINE"+ Style.RESET_ALL, end="")
print(Fore.BLACK + Style.DIM + "\n======================================\n++++++++++++++++++++++++++++++++++++++\n======================================\n"+ Style.RESET_ALL)


def handle_click():
    theInput = entry.get()
    if len(theInput) > 40:
        label.config(text = Fore.RED + "\nPlease follow the guidelines in *help* when making your request\n" + Style.RESET_ALL, font= ('Helvetica 13'))
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
                        label.config(text = Fore.RED + "\nImproper Input Format\n" + Style.RESET_ALL, font= ('Helvetica 13'))
                else:
                    label.config(text = Fore.RED + "\nImproper Input Format\n" + Style.RESET_ALL, font= ('Helvetica 13'))
            else:
               label.config(text = Fore.RED + "\Error. REquest not Recognized\n" + Style.RESET_ALL, font= ('Helvetica 13'))
        elif userInput[0] == 'buy' and len(userInput) > 1:
            if userInput[1] == 'item':
                inputCheck = buyItemFunc(userInput, priceInput)
            else: 
                print(Fore.RED + "\nError. Request not recognized\n" + Style.RESET_ALL)
            if inputCheck == -1:
                print(Fore.RED + "\nImproper Input Format\n" + Style.RESET_ALL)           
        elif userInput[0] == 'balance':
            print(Fore.GREEN + "\nThe current currency of the vending machine is as follows:" + Style.RESET_ALL)
            print(Fore.GREEN + "", vendingMoney.dollars, Fore.BLACK + "dollars", Fore.GREEN + "", vendingMoney.quarters, Fore.BLACK + "quarters", Fore.GREEN + "", vendingMoney.dimes, Fore.BLACK + "dimes", Fore.GREEN + "", vendingMoney.nickels, Fore.BLACK + "nickels", Fore.GREEN + "", vendingMoney.pennies, Fore.BLACK + "pennies")
            print(Fore.GREEN + "The total balance of the vending machine is:", Style.BRIGHT + "${:,.2f}".format(vendingMoney.dollars + vendingMoney.quarters*.25 + vendingMoney.dimes*.10 + vendingMoney.nickels*.05 + vendingMoney.pennies*.01), "\n" + Style.RESET_ALL)
        elif userInput[0] == 'inventory':
            vending.printInv()  
        elif userInput[0] == 'history':
            print(Fore.YELLOW + Style.BRIGHT + "\nThe following transactions have been requested:" + Style.RESET_ALL + Fore.YELLOW)
            for i in range(0, len(history)):
                print(i+1, history[i])
            print(Style.RESET_ALL)
        elif userInput[0] == 'help':
            print(Fore.RED + Style.BRIGHT + "\nTo navigate the vending machine, please use one of the following commands:" + Style.RESET_ALL)
            print(Fore.RED + "[add item name quantity $price]\t\t", Fore.LIGHTRED_EX + "Adds an item to the vending machine if it does not already exist. Must use '$'" + Style.RESET_ALL)
            print(Fore.RED + "[balance]\t\t\t\t", Fore.LIGHTRED_EX + "Shows the current balance of the vending machine" + Style.RESET_ALL)
            print(Fore.RED + "[buy item name #dollars #quarters #dimes #nickels #pennies]", Fore.LIGHTRED_EX + "Buys an item from the vending machine. NOTE: Zeros must be inputted for any currency not used" + Style.RESET_ALL)
            print(Fore.RED + "[exit]\t\t\t\t\t", Fore.LIGHTRED_EX + "Exits the vending machine" + Style.RESET_ALL)
            print(Fore.RED + "[help]\t\t\t\t\t", Fore.LIGHTRED_EX + "Displays the help table" + Style.RESET_ALL)
            print(Fore.RED + "[history]\t\t\t\t", Fore.LIGHTRED_EX + "Shows the previous requested transactions" + Style.RESET_ALL)
            print(Fore.RED + "[inventory]\t\t\t\t", Fore.LIGHTRED_EX + "Shows the current inventory of the vending machine\n" + Style.RESET_ALL)
        elif userInput[0] == 'exit':
            window.destroy()
            print(Fore.BLACK + Style.DIM + "\n=====================================================================\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n=====================================================================" + Style.RESET_ALL)
            print(Fore.BLUE + Style.BRIGHT + "THANK YOU FOR VISITING THE ULTIMATE VENDING MACHINE. HAVE A GOOD DAY"+ Style.RESET_ALL, end="")
            print(Fore.BLACK + Style.DIM + "\n=====================================================================\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n====================================================================="+ Style.RESET_ALL)
            
        else:
            print(Fore.RED + "\nError. Request not recognized\n" + Style.RESET_ALL)
        properChange.dollars = 0
        properChange.quarters = 0
        properChange.dimes = 0
        properChange.nickels = 0
        properChange.pennies = 0
        inputCheck = 0
        twoWords = -1

print("Hello")
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
                 #background="#34A2FE",
                 ##size of our working canvas
                 width = 1000,
                 height = 800,
                 image = newImg)
##adds the greeting to our window

'''
entryLabel = tk.Label(text = "Please input your request here")
entry = tk.Entry(fg="black", bg="yellow", width=50)

entryLabel.pack()
entry.pack()
input = entry.get()
print(input)
'''


def get_data():
   label.config(text= entry.get(), font= ('Helvetica 13'))

#Create an Entry Widget
entry = tk.Entry(window, width= 42)
entry.place(relx= .47, rely= .87, anchor= "center")

#Inititalize a Label widget
label2= tk.Label(window, text="", font=('Helvetica 13'))
frame.pack()
label.pack()
label2.pack()

#Create a Button to get the input data
button = tk.Button(window, text= "Push", command= handle_click).place(relx= .4, rely= .8, anchor= "center")
'''button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)'''
#button.bind("<Button-1>", handle_click)

##runs out previous window applications
window.mainloop()
