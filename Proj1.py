class myInventory:
    def __init__(self, ID, name, quantity, price):
        self.ID = ID
        self.name = name
        self.quantity = quantity
        self.price = price
    def get_info(self):
        return f"{self.ID}, {self.name}, {self.quantity}, '$'{self.price}"
    def __len__(self):
        return len(self)

#intializing variables
myBalance = 40
history = []
item1 = myInventory(1, 'oreos', 3, 2.50)
item2 = myInventory(2, 'reeses', 8, 2.80)
item3 = myInventory(3, 'cheezits', 6, 3.00)
print(item3)

#start the input validation and output
while True:

    userInput = input("What would you like to see? ").split()
    history.append(userInput)

    if userInput[0] == 'buy' and len(userInput) > 1:
        if userInput[1] == 'item':
            #for i in range(0,len(myInventory)):
               # if myInventory[i] == userInput[2]:
               print("im here")
        else: 
            print("Error. Request not recognized")

    elif userInput[0] == 'balance':
        print("Your balance is", myBalance)

    elif userInput[0] == 'inventory':
        for i in range(0, 4):
            print(myInventory)
            
    elif userInput[0] == 'history':
        print("The following transactions have been requested:")
        for i in range(0, len(history)):
            print(history[i])
    elif userInput[0] == 'exit':
        print("Thank you for visiting. Have a nice day!")
        break
    else:
        print("Error. Request not recognized")


#def inventory