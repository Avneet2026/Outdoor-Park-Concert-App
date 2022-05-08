import json
from json.decoder import JSONDecodeError

"""
This example code creates a 2d list (2d matrix) that can store seating.
The matrix is populated with a since all seats are available
"""

# our test matrix has 20 rows and 26 columns
import re


n_row = 20
n_col = 26
FRONT_ROW_PRICE = 80
MIDDLE_ROW_PRICE = 50
BACK_ROW_PRICE = 25
MASK_FEE = 5
REGEX = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
alphaToNum = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7,
             'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14,
             'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21,
             'w':22, 'x':23, 'y':24, 'z':25}

# available seat
available_seat = 'a'
unavailable_seat = 'X'
# create some available seating
seating = []

def CreateSeating():
    for r in range(n_row):
        row = []
        for c in range(n_col):
            row.append(available_seat)
        seating.append(row)

def PrintSeating():
    # print available seating
    print('\t' + "a b c d e f g h i j k l m n o p q r s t u v w x y z")
    for r in range(n_row):
        print(r, end="\t")
        for c in range(n_col):
            print(seating[r][c], end=" ")
        print()

def SeatPricing():
    # print seating prices
    print()
    print("Front Rows price:  $80, Rows 0-4")
    print("Middle Rows price: $50, Rows 5-10")
    print("Back Rows price:   $25, Rows 11-19")
    print()

def CheckRowSize(seat):
    if len(seat) == 3:
        row = int(seat[0:2])
        column = alphaToNum[seat[2]]
    else:
        row = int(seat[0])
        column = alphaToNum[seat[1]]
    return row, column

def CheckAvail(seat):
    row, column = CheckRowSize(seat)
    if row in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]:
        print("Sorry, all odd rows are unavailable due to COVID restrictions.")
        return False
    elif seating[row][column] == 'X':
        print("Sorry, this seat is occupied.")
        return False
        
    if column == 24:
        if seating[row][column+1] == 'X' or seating[row][column-1] == 'X' or seating[row][column-2] == 'X':
            print("Sorry, this seat is unavailable due to COVID restrictions.")
            return False
    elif column == 25:
        if seating[row][column-1] == 'X' or seating[row][column-2] == 'X':
            print("Sorry, this seat is unavailable due to COVID restrictions.")
            return False
    else:
        if seating[row][column+1] == 'X' or seating[row][column+2] == 'X' or seating[row][column-1] == 'X' or seating[row][column-2] == 'X':
            print("Sorry, this seat is unavailable due to COVID restrictions.")
            return False

def BuyTickets(purchaseList):
    ticketCosts = 0
    for x in purchaseList:
        row, column = CheckRowSize(x)
        seating[row][column] = 'X'
        if (0 <= row <= 4):
            ticketCosts = ticketCosts + FRONT_ROW_PRICE
        elif (5 <= row <= 10):
            ticketCosts = ticketCosts + MIDDLE_ROW_PRICE
        elif (11 <= row <= 19):
            ticketCosts = ticketCosts + BACK_ROW_PRICE

    tax = 0.0725*ticketCosts    
    totalCost = ticketCosts + tax + MASK_FEE
    print()
    print("------------------------")
    print("--- PURCHASE SUMMARY ---")
    print("------------------------")
    print(f"Subtotal   = ${ticketCosts:.2f}")
    print(f"State Tax  = ${tax:.2f}")
    print(f"Mask Fee   = ${MASK_FEE:.2f}")
    print(f"Total Cost = ${totalCost:.2f}")

    print()
    print()
    while True:
        userName = input("Please enter your name:   ").lower()
        if not (userName == ""):
            break
        else:
            print("Error! Name cannot be blank.")
    while True:
        userEmail = input("Please enter your email:  ")
        if re.fullmatch(REGEX, userEmail):
            break
        else:
            print("Error! Please provide a valid email address.")

    jsonData.append({
        "name": userName,
        "numTickets": len(purchaseList),
        "seats": purchaseList,
        "email": userEmail,
        "totalCost": totalCost
    })
    with open("SavedSeatPurchases.json", 'w+') as json_file:
        json.dump(jsonData, json_file, indent = 4, separators=(',',': '))


userQuit = False
CreateSeating()
with open("SavedSeatPurchases.json", "r+") as myJson:
    try:
        jsonData = json.load(myJson)
        for customer in jsonData:
            for x in customer['seats']:
                row, column = CheckRowSize(x)
                seating[row][column] = 'X'
    except JSONDecodeError:
        jsonData=[]
        print("File was empty, creating an empty list")

while (not userQuit):
    # menu
    print()
    print("•••••••••••••••••••••••")
    print("Welcome to the Concert!")
    print("•••••••••••••••••••••••")
    print()
    print("[B] buy a ticket")
    print("[D] display all purchases")
    print("[S] search by name")
    print("[V] view available seating")
    print("[Q] quit")
    print()

    # get the user input
    userInput = input("Enter a command:")
    lowerInput = userInput.lower()
    firstChar = lowerInput[0:1]

    # quit
    if firstChar == 'q':
        userQuit = True
        print()
        print("Thank you for purchasing tickets for the concert!!")
        print()
    
    # buy a ticket
    elif firstChar == 'b':
        """
        - provide receipt with state tax of 7.25%
        - additional mandatory mask fee of $5
        - when purchase is made ask for name and email address
        """

        PrintSeating()
        SeatPricing()
        while True:
            numTickets = input("How many tickets would you like to buy?  ")
            if not (numTickets == ""):
                numTickets = int(numTickets)
                break
            else:
                print("Error! Number of tickets you are buying cannot be blank.")
        ticketList = []
        print()
        print("All odd rows are unavailable due to COVID restrictions.")
        print("When you choose your seat make sure to enter row number and column letter.")
        print("For example: row 2 column c would be 2c")
        print()
        for x in range(numTickets):
            while True:
                seatChoice = input(f"Pick seat #{x+1} (m to go to menu):  ").lower()
                if (seatChoice == ""):
                    print("Error! Seat choice cannot be blank.")
                    continue
                if seatChoice == 'm':
                    break
                if CheckAvail(seatChoice) == False:
                    continue
                else:
                    ticketList.append(seatChoice)
                    break
            if seatChoice == 'm':
                break
            
        if seatChoice != 'm':
            BuyTickets(ticketList)


    # display all purchases
    elif firstChar == 'd':
        """
        - prints all purchases made
        - shows the total amount of money the venue has made
        """
        venueMoney = 0
        for customerPurchase in jsonData:
            print(f"Customer ({customerPurchase['name']}) purchased {customerPurchase['numTickets']} ticket(s). Total price paid was ${customerPurchase['totalCost']:.2f}.")
            venueMoney = venueMoney + customerPurchase['totalCost']
        print()
        print(f"The total money the venue has made is ${venueMoney}")

    
    # search by name
    elif firstChar == 's':
        """
        - displays tickets purchased by user with specific name
        """
        lookupUser = input("Please enter customers name to lookup tickets purchased:  ").lower()
        for customer in jsonData:
            if lookupUser == customer['name']:
                print()
                print(f"Customer ({lookupUser}) purchased {customer['numTickets']} ticket(s). Seat(s) are {customer['seats']}.")
                break
        else:
            print()
            print("Error! Customer not found.")

    # view available seating
    elif firstChar == 'v':
        """
        - available seats are indicated with a lower case a
        - occupied seats are indicated with a capital X
        - 2 social distancing seats between each occupied seat on a row
        - 1 row distance between each row
        - bulk tickets can sit next to each other
        - 3 types of seating
            - front seat price $80
                - rows 0 - 4
            middle seat price $50
                - rows 5 - 10
            - back seat price $ 25
                - rows 11 - 19
        """
        PrintSeating()