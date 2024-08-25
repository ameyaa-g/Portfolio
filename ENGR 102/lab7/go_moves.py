
# Make the list 9 by 9
# Intialize the Board list with 9 columns
# Each aspect of the list has 9 rows
# Have it be intialized into being full of periods
Board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

# Print the instructions
print('Type the coordinates you want to change. Print stop to end the game')
for i in range(len(Board)):
    for j in Board[i]:
        print(j, end=" ")
    print()
# Initialize a counter, which decides if it is white or black turn
counter = 1
turnx = input("White's turn: X coordinate:")
turny = input("White's turn: Y coordinate")
# Have a loop, which takes an input from the user (While loop – while the input is not stop)
while turnx != 'stop' or turny != 'stop':
    # add one to the counter
    counter += 1
    # Coordinate
    # If the coordinate is not period, don’t place and return an error
    x = int(turnx)
    y = int(turny)
    if '.' in Board[x][y]:
        # Have an if statement to see if it is white or black turn
        if counter % 2 == 0:
            # Change the dot at the coordinate accordingly
            Board[x][y] = chr(9679)
            # Print the lists
            for i in range(len(Board)):
                for j in Board[i]:
                    print(j, end=" ")
                print()
            turnx = input("Black's turn: X coordinate:")
            turny = input("Black's turn: Y coordinate")
        elif counter % 2 != 0:
            Board[x][y] = chr(9675)
            # Print the lists
            for i in range(len(Board)):
                for j in Board[i]:
                    print(j, end=" ")
                print()
            turnx = input("White's turn: X coordinate:")
            turny = input("White's turn: Y coordinate")
    else:
        print('There is already a piece there')
        counter -= 1
        if counter % 2 == 0:
            turnx = input("Black's turn: X coordinate:")
            turny = input("Black's turn: Y coordinate")
        elif counter % 2 != 0:
            turnx = input("White's turn: X coordinate:")
            turny = input("White's turn: Y coordinate")




