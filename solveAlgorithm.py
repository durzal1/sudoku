import time
import pygame
import random
import copy
class solveAlgorithm:
    def __init__(self, win, HEIGHT, WIDTH, grid):
        # constants
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH

        # pygame variables
        self.win = win

        # grid values that we know are right from the start
        self.grid = grid

        # perfect grid with all answers
        self.answers = []

        # grid that also contains guesses
        self.guessGrid = []

        # create the foundation of guessGrid and answers(this being grid)
        for i in range(9):
            self.guessGrid.append([])
            self.answers.append([])
            for j in range(9):
                self.guessGrid[i].append(self.grid[i][j])
                self.answers[i].append(self.grid[i][j])

        # play sudoku
        self.play()

    # lets the user play sudoku and fill in answers themselves
    def play(self):
        # space between spots
        space = self.WIDTH // 14
        space2 = self.HEIGHT // 9

        # constants
        xConst = 30
        yConst = 10
        gray = (220, 220, 220)
        black = (0,0,0)

        # draws lines
        for i in range(9):
            if (i % 3 == 0):
                pygame.draw.line(self.win, black, (i * space2, 0), (i * space2, self.HEIGHT))
            else:
                pygame.draw.line(self.win, gray, (i * space2, 0), (i * space2, self.HEIGHT))
            pygame.display.flip()

        for i in range(9):
            if (i % 3 == 0):
                pygame.draw.line(self.win, black, (0, i * space2), (self.HEIGHT, i * space2))
            else:
                pygame.draw.line(self.win, gray, (0, i * space2), (self.HEIGHT, i * space2))

            pygame.display.flip()

        # draws grid
        for i in range(9):
            for j in range(9):
                # empty space
                if self.grid[i][j] == 0:
                    continue

                font = pygame.font.SysFont('arial', 50)
                text = font.render(str(self.grid[i][j]), True, black)
                self.win.blit(text, (i * space2 + xConst, j * space2 + yConst))
                pygame.display.update()

        # i(y axis value) will be set to the right of the screen
        i = self.WIDTH - 100

        # adds all the numbers and "check" button
        for j in range(10):
            text = str(j+1)
            color = (0,0,0)
            if j == 9:
                # here we write finish instead
                text = "Finish"
                i -= 40

                # change to green
                color = (0,255,0)

            font = pygame.font.SysFont('arial', 50)
            text = font.render(text, True, color)
            self.win.blit(text, (i, j*space))
            pygame.display.update()

        # what number is currently selected from the right side
        currentNumSelected = None

        # main loop for playing game
        while True:
            for event in pygame.event.get():
                #if user exits
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # handle MOUSEBUTTONUP
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    if pos[0] > 745:
                        # which number has been selected +1
                        num = pos[1] // space
                        currentNumSelected = num + 1

                        # if its over 9 then they want to remove the empty space
                        if num > 9:
                            # changes currentNumSelected to 0 so it can be changed
                            currentNumSelected = 0
                        # if its 9 then user is finished
                        elif num == 9:
                            # first we find what the first unknown is and give it options to chose from
                            found = False
                            firstI = -1
                            firstJ = -1
                            for I in range(9):
                                for J in range(9):
                                    if self.grid[I][J] == 0:
                                        # documents the I and J
                                        firstI = I
                                        firstJ = J
                                        found = True
                                        break
                                if found:
                                    break
                            # give it options to chose from
                            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                            solutions = [0]
                            # run through each option till solutions[0] returns 1
                            for i in range(9):
                                # we check the users answers
                                self.backtracking(nums[i],firstI, firstJ,self.answers,solutions)

                                # if it found the solution
                                if (solutions[0] == 1):
                                    # draws the solution
                                    for I in range(9):
                                        for J in range(9):

                                            # an answer that is 100% known to user
                                            if self.grid[I][J] == 0:
                                                # checks whether user is right or wrong
                                                if self.answers[I][J] == self.guessGrid[I][J]:
                                                    # user is right
                                                    pygame.draw.rect(self.win, (255, 255, 255), (I * space2 + 5, J * space2 + 5, space2 - 10, space2 - 10))
                                                    pygame.display.update()

                                                    # draws the number
                                                    font = pygame.font.SysFont('arial', 50)
                                                    text = font.render(str(self.answers[I][J]), True, (0, 255, 0))
                                                    self.win.blit(text, (I * space2 + xConst, J * space2 + yConst))
                                                    pygame.display.update()

                                                else:
                                                    # user is wrong
                                                    pygame.draw.rect(self.win, (255, 255, 255), (
                                                    I * space2 + 5, J * space2 + 5, space2 - 10, space2 - 10))
                                                    pygame.display.update()

                                                    # draws the number
                                                    font = pygame.font.SysFont('arial', 50)
                                                    text = font.render(str(self.answers[I][J]), True, (255, 0, 0))
                                                    self.win.blit(text, (I * space2 + xConst, J * space2 + yConst))
                                                    pygame.display.update()

                                    pygame.display.update()

                                    # program is finished and user can look at the answer
                                    time.sleep(10)
                                    pygame.quit()
                                    exit()



                    # inputting an answer
                    elif currentNumSelected != None:
                        # gets the i,j of it
                        i = pos[0] // space2
                        j = pos[1] // space2

                        # makes sure it is not a confirmed solution
                        if self.grid[i][j] == 0:
                            # replaces it in the guessGrid
                            self.guessGrid[i][j] = currentNumSelected

                            # incase it already has a guess we clear the spot with a white square
                            pygame.draw.rect(self.win, (255,255,255), (i*space2+5, j*space2+5, space2-10, space2-10))
                            pygame.display.update()

                            if self.guessGrid[i][j] != 0:
                                # draws the number
                                font = pygame.font.SysFont('arial', 50)
                                text = font.render(str(currentNumSelected), True, (0, 0, 255))
                                self.win.blit(text, (i * space2 + xConst, j * space2 + yConst))
                                pygame.display.update()

    # checks all the answers of user
    def backtracking(self, num, i, j, grid, solutions):
        newGrid = copy.deepcopy(grid)

        # check each row
        for row in range(9):
            if grid[row][j] == num:
                return False

        # check each column
        for column in range(9):
            if grid[i][column] == num:
                return False

        # check which box it belongs to
        rowBox = (j) // 3
        columnBox = (i) // 3

        # check each box
        for row in range(1, 4):
            for column in range(1, 4):
                x = column + 3 * columnBox - 1
                y = row + 3 * rowBox - 1
                if grid[x][y] == num:
                    return False

        ## passed all of the checks

        # we set the i,j to the grid
        newGrid[i][j] = num

        perfect = True
        # if every grid spot has a value (base case)
        for I in range(9):
            for J in range(9):
                if newGrid[I][J] == 0:
                    perfect = False
        if perfect:
            # found solution
            solutions[0] += 1

            # we update self.answers
            self.answers = newGrid
            return solutions

        # iterates through each new position to look for an empty space
        newSpaceI = -1
        newSpaceJ = -1
        found = False
        for I in range(i, 9):
            for J in range(0, 9):
                # makes sure it doesnt pass something thats already been run
                if I == i and J <= j:
                    continue
                if newGrid[I][J] == 0:
                    newSpaceI = I
                    newSpaceJ = J
                    found = True
                    break
            if found:
                break

        # nums left to try for the spot
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # while there are still more options that can be tried for the current spot
        while (len(nums) != 0):
            newNumInd = random.randint(0, len(nums) - 1)
            newNum = nums[newNumInd]

            # recursivly call function
            ret = self.backtracking(newNum, newSpaceI, newSpaceJ, newGrid, solutions)

            # the value we tried did not work
            if (ret == False):
                # we delete it from the nums options
                nums.pop(newNumInd)
            else:
                # found solution
                return ret

        # no more options left to try so its done
        if len(nums) == 0:
            return False
