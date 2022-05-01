"""
This example code creates a 2d list (2d matrix) that can store seating.
The matrix is populated with a since all seats are available
"""

# our test matrix has 20 rows and 26 columns
n_row = 20
n_col = 26
alphaToNum ={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7,
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
    print("Front Rows price: $80, Rows 0-4")
    print("Middle Rows price: $50, Rows 5-10")
    print("Back Rows price: $25, Rows 11-19")
    print()

def CheckAvail(seat):
    row = int(seat[0])
    column = alphaToNum[seat[1]]
    if seating[row][column] == '-':
        print("Sorry, this seat is unavailable due to COVID restrictions.")
        return False
    elif seating[row][column] == 'X':
        print("Sorry, this seat is occupied.")
        return False

def BuyTickets(purchaseList):
    for x in purchaseList:
        row = int(x[0])
        column = alphaToNum[x[1]]
        seating[row][column] = 'X'
    PrintSeating()


userQuit = False
CreateSeating()
while (not userQuit):
    # menu
    print()
    print("-----------------------")
    print("Welcome to the Concert!")
    print("-----------------------")
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
    
    # buy a ticket
    elif firstChar == 'b':
        """
        - provide receipt with state tax of 7.25%
        - additional mandatory mask fee of $5
        - when purchase is made ask for name and email address
        """

        PrintSeating()
        SeatPricing()

        numTickets = int(input("How many tickets would you like to buy?  "))
        ticketList = []
        print()
        print("When you choose your seat make sure to enter row number and column letter.")
        print("For example: row 1 column c would be 1c")
        print()
        for x in range(numTickets):
            while True:
                seatChoice = input(f"Pick seat #{x+1} (m to go to menu):  ").lower()
                if seatChoice == 'm': # need to fix
                    break
                if CheckAvail(seatChoice) == False:
                    continue
                else:
                    ticketList.append(seatChoice)
                    break
            
        if seatChoice != 'm':
            BuyTickets(ticketList)

        
        # p = 
        # tax = 0.0725(p)
        # maskFee = 5
        # total = p + tax + maskFee


    # display all purchases
    elif firstChar == 'd':
        """
        - prints all purchases made
        - shows the total amount of money the venue has made
        """
    # search by name
    elif firstChar == 's':
        """
        - displays tickets purchased by user with specific name
        """

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