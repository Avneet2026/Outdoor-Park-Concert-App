"""
This example code creates a 2d list (2d matrix) that can store seating.
The matrix is populated with a since all seats are available
"""

userQuit = False
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


    # our test matrix has 20 rows and 26 columns
    n_row = 20
    n_col = 26

    # available seat
    available_seat = 'a'
    unavailable_seat = 'X'

    # create some available seating
    seating = []
    for r in range(n_row):
        row = []
        for c in range(n_col):
            row.append(available_seat)
        seating.append(row)

    # print available seating
    for r in range(n_row):
        print(r+1, end="\t")
        for c in range(n_col):
            print(seating[r][c], end=" ")
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