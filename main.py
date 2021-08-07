from tkinter import *
from createBoard import *
from solveAlgorithm import *
import pickle
import os

## constants

# for the screen size
WIDTH = 768 + 142 # 142 is the amount we put on the bar to the right with numbers
HEIGHT = 768 - 40 # -40 cuz thats about how much the top bar is

# for the button size
PADX = 80
PADY = 50

# what difficulty the game will run at
difficulty = None

# inits pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")
WIN.fill((255,255,255))

# inits tkinter to either create puzzles or play them
root = Tk()
root.geometry("500x150")

# options user can choose
def Create():
    global choice
    choice = "create"
    root.destroy()


def Play():
    global choice
    choice = "play"
    root.destroy()

#buttons that will visually display the options
myButton1 = Button(root, text="Create", command=Create, padx=PADX, pady=PADY, fg="white",  bg="green")
myButton2 = Button(root, text="Play", command=Play, padx=PADX, pady=PADY, fg="white",  bg="blue")

myButton1.grid(row=0,column=0, pady=10, padx= 15)
myButton2.grid(row=0, column=1, pady=10, padx= 15)

root.mainloop()

# user will play a puzzle of their choice
if choice == "play":
    #inits tkinter to choose what they will play
    root = Tk()
    root.geometry("1000x150")

    # options user can choose
    def Beginner():
        global Grid
        # total amount of puzzles
        db = open('numBeginner', 'rb')
        amount = pickle.load(db)

        # loads last grid
        dbfile = open(f'Beginner{amount - 1}', 'rb')
        Grid = pickle.load(dbfile)

        db.close()
        dbfile.close()

        # deletes numBeginner and re-adds it by decreasing numBeginner by 1
        # since you are deleting one puzzle from it
        os.remove("numBeginner")

        dbfile = open('numBeginner', 'ab')

        # source, destination
        pickle.dump(amount-1, dbfile)

        dbfile.close()

        # deletes the puzzle
        os.remove(f"Beginner{amount - 1}")

        root.destroy()


    def Intermediate():
        global Grid
        # total amount of puzzles
        db = open('numIntermediate', 'rb')
        amount = pickle.load(db)

        # loads last grid
        dbfile = open(f'Intermediate{amount - 1}', 'rb')
        Grid = pickle.load(dbfile)

        db.close()
        dbfile.close()

        # deletes numBeginner and re-adds it by decreasing numBeginner by 1
        # since you are deleting one puzzle from it
        os.remove("numIntermediate")

        dbfile = open('numIntermediate', 'ab')

        # source, destination
        pickle.dump(amount - 1, dbfile)

        dbfile.close()

        # deletes the puzzle
        os.remove(f"Intermediate{amount - 1}")

        root.destroy()

    def Advanced():
        global Grid
        # total amount of puzzles
        db = open('numAdvanced', 'rb')
        amount = pickle.load(db)

        # loads the last grid
        dbfile = open(f'Advanced{amount - 1}', 'rb')
        Grid = pickle.load(dbfile)

        db.close()
        dbfile.close()

        # deletes numBeginner and re-adds it by decreasing numBeginner by 1
        # since you are deleting one puzzle from it
        os.remove("numAdvanced")

        dbfile = open('numAdvanced', 'ab')

        # source, destination
        pickle.dump(amount - 1, dbfile)

        dbfile.close()

        # deletes the puzzle
        os.remove(f"Advanced{amount - 1}")

        root.destroy()

    def Expert():
        global Grid
        # total amount of puzzles
        db = open('numExpert', 'rb')
        amount = pickle.load(db)

        # loads the last grid
        dbfile = open(f'Expert{amount - 1}', 'rb')
        Grid = pickle.load(dbfile)

        db.close()
        dbfile.close()

        # deletes numBeginner and re-adds it by decreasing numBeginner by 1
        # since you are deleting one puzzle from it
        os.remove("numExpert")

        dbfile = open('numExpert', 'ab')

        # source, destination
        pickle.dump(amount - 1, dbfile)

        dbfile.close()

        # deletes the puzzle
        os.remove(f"Expert{amount - 1}")

        root.destroy()

    #buttons that will visually display the options
    myButton1 = Button(root, text="Beginner", command=Beginner, padx=PADX, pady=PADY, fg="white",  bg="green")
    myButton2 = Button(root, text="Intermediate", command=Intermediate, padx=PADX, pady=PADY, fg="white",  bg="blue")
    myButton3 = Button(root, text="Advanced", command=Advanced, padx=PADX, pady=PADY, fg="white",  bg="orange")
    myButton4 = Button(root, text="Expert", command=Expert, padx=PADX, pady=PADY, fg="white",  bg="red")
    myButton1.grid(row=0,column=0, pady=10, padx= 15)
    myButton2.grid(row=0, column=1, pady=10, padx= 15)
    myButton3.grid(row=0, column=2, pady=10, padx= 15)
    myButton4.grid(row=0, column=3, pady=10, padx= 15)
    root.mainloop()

    # make grid into a 9x9 array
    goodGrid = []
    for i in range(9):
        goodGrid.append([])
        for j in range(9):
            goodGrid[i].append(Grid[i][j])
    solveAlgorithm(WIN, HEIGHT, WIDTH, goodGrid)







# creating new mazes
print("write how many Beginner, intermediate, advanced, and expert puzzels wanted in that order")
numBeginner = int(input())
numIntermediate = int(input())
numAdvanced = int(input())
numExpert = int(input())

## stores how many of each difficulty there are

# first checks if the file exists so it can delete it
## If file exists, delete it ##
if os.path.isfile("numBeginner"):
    #checks how many of each there are

    # total amount of puzzles
    db = open('numBeginner', 'rb')
    amount = pickle.load(db)

    #iteates through each of them and delete each one
    for i in range(amount):
        os.remove(f"Beginner{i}")
    db.close()
    os.remove("numBeginner")


    db = open('numIntermediate', 'rb')
    amount = pickle.load(db)

    # iteates through each of them and delete each one
    for i in range(amount):
        os.remove(f"Intermediate{i}")
    db.close()
    os.remove("numIntermediate")


    db = open('numAdvanced', 'rb')
    amount = pickle.load(db)

    # iteates through each of them and delete each one
    for i in range(amount):
        os.remove(f"Advanced{i}")
    db.close()
    os.remove("numAdvanced")


    db = open('numExpert', 'rb')
    amount = pickle.load(db)

    # iteates through each of them and delete each one
    for i in range(amount):
        os.remove(f"Expert{i}")
    db.close()
    os.remove("numExpert")

# pickles each amount
dbfile = open('numBeginner', 'ab')

# source, destination
pickle.dump(numBeginner, dbfile)
dbfile.close()


# intermediate
dbfile = open('numIntermediate', 'ab')

# source, destination
pickle.dump(numIntermediate, dbfile)
dbfile.close()


# Advanced
dbfile = open('numAdvanced', 'ab')

# source, destination
pickle.dump(numAdvanced, dbfile)
dbfile.close()


# Expert
dbfile = open('numExpert', 'ab')

# source, destination
pickle.dump(numExpert, dbfile)
dbfile.close()

# creates the amount of puzzles wanted by the user
for i in range(int(numBeginner)):
    difficulty = "Beginner"
    Board = createBoard(difficulty, HEIGHT, WIDTH- 142)

    # save the grid of the board to be used later on (pickle)
    dbfile = open(f'Beginner{i}', 'ab')

    # source, destination
    pickle.dump(Board.grid, dbfile)
    dbfile.close()
    print(f'Beginner{i}')

for i in range(int(numIntermediate)):
    difficulty = "Intermediate"
    Board = createBoard(difficulty, HEIGHT, WIDTH - 142)

    # save the grid of the board to be used later on (pickle)
    dbfile = open(f'Intermediate{i}', 'ab')

    # source, destination
    pickle.dump(Board.grid, dbfile)
    dbfile.close()
    print(f'Intermediate{i}')

for i in range(int(numAdvanced)):
    difficulty = "Advanced"
    Board = createBoard(difficulty, HEIGHT, WIDTH - 142)

    # save the grid of the board to be used later on (pickle)
    dbfile = open(f'Advanced{i}', 'ab')

    # source, destination
    pickle.dump(Board.grid, dbfile)
    dbfile.close()
    print(f'Advanced{i}')

for i in range(int(numExpert)):
    difficulty = "Expert"
    Board = createBoard(difficulty, HEIGHT, WIDTH - 142)

    # save the grid of the board to be used later on (pickle)
    dbfile = open(f'Expert{i}', 'ab')

    # source, destination
    pickle.dump(Board.grid, dbfile)
    dbfile.close()
    print(f'Expert{i}')