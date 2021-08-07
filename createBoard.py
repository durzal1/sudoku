import random
import copy


class createBoard:

    def __init__(self, diff, HEIGHT, WIDTH):
        # constants
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH

        # difficulty
        self.diff = diff

        # grid values
        self.grid = []


        # all possible values for each position
        self.possibleValues = []

        #creates the original grid
        self.createGrid()

        # removes elements to create the puzzle
        self.removeElements()

        # #draws grid
        # self.drawGrid()

    # removes points from the puzzle
    def removeElements(self):
        # puts every possible pos in a list(81)
        possiblePos = []

        for i in range(81):
            possiblePos.append(i)

        # each point on the grid will use on these points
        gridPos = {}
        for i in range(9):
            for j in range(9):
                # gets a random point and removes it so it cannot be used again
                ind = random.randint(0,len(possiblePos) - 1)

                # adds it to a dictionary so it can easily be called later
                gridPos[possiblePos[ind]] = [i,j]

                possiblePos.pop(ind)

        # iterate through the dictionary
        count = 0
        for i in range(81):
            val = gridPos[i]

            # creates a temp grid and removes the val from it
            tempGrid = copy.deepcopy(self.grid)
            tempGrid[val[0]][val[1]] = 0

            # look for the first value in the grid that does not have a value yet
            firstI = -1
            firstJ = -1
            found = False
            for I in range(9):
                for J in range(9):
                    if tempGrid[I][J] == 0:
                        # documents the I and J
                        firstI = I
                        firstJ = J
                        found = True
                        break
                if found:
                    break

            # runs a backtracking algorithm to find how many solutions it has
            solutions = [0]
            nums = [1,2,3,4,5,6,7,8,9]
            for I in range(9):
                self.backtrackingSolve(nums[I], firstI, firstJ, tempGrid, solutions)
            if solutions[0] == 1:
                # deletes the value from the real grid
                self.grid[val[0]][val[1]] = 0
                count+= 1

            # this is how many open spots there are the more the longer it takes(after 44 takes a super long time)
            # the less count is the easier it is. This is how we choose difficulty

            # beginner
            if count == 30 and self.diff == "Beginner":
                break

            #intermediate
            if count == 40 and self.diff == "Intermediate":
                break

            # advanced
            if count == 50 and self.diff == "Advanced":
                break

            # for expert we let it run through all 81 to get the most open spaces possible


    # backtracking function to solve the grid
    def backtrackingSolve(self, num, i, j, grid, solutions):
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
            # created a working game
            solutions[0] += 1
            return False

        # iterates through each new position to look for an empty space
        newSpaceI = -1
        newSpaceJ = -1
        found = False
        for I in range(i,9):
            for J in range(0,9):
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
            ret = self.backtrackingSolve(newNum, newSpaceI, newSpaceJ, newGrid, solutions)

            # the value we tried did not work
            if (ret == False):
                # we delete it from the nums options
                nums.pop(newNumInd)


        # no more options left to try so its done
        if len(nums) == 0:
            return False

    # draws the elements on the grid
    #### dont really need this anymore since program only draws in solveAlgorithm
    # def drawGrid(self):
    #     # space between spots
    #     space = self.WIDTH // 9
    #
    #     # constants to make it look nicer
    #     xConst = 30
    #     yConst = 10
    #     gray = (220,220,220)
    #     black = (0,0,0)
    #
    #     # draws lines
    #     for i in range(9):
    #         if (i % 3 == 0):
    #             pygame.draw.line(self.win, black, (i * space, 0), (i * space, self.HEIGHT))
    #         else:
    #             pygame.draw.line(self.win, gray, (i * space, 0), (i * space, self.HEIGHT))
    #         pygame.display.flip()
    #
    #     for i in range(9):
    #         if (i % 3 == 0):
    #             pygame.draw.line(self.win, black, (0, i * space), (self.HEIGHT, i * space))
    #         else:
    #             pygame.draw.line(self.win, gray, (0, i * space), (self.HEIGHT, i * space))
    #
    #         pygame.display.flip()
    #
    #     for i in range(9):
    #         for j in range(9):
    #             # empty space
    #             if self.grid[i][j] == 0:
    #                 continue
    #
    #             font = pygame.font.SysFont('arial', 50)
    #             text = font.render(str(self.grid[i][j]), True, (0,0, 255))
    #             self.win.blit(text,(i*space+xConst, j*space+yConst))
    #             pygame.display.update()
    #     # time.sleep(900000)

    def createGrid(self):
        # iterates through each row and column and sets it to 0
        for i in range(9):
            self.grid.append([])
            self.possibleValues.append([])
            for j in range(9):
                self.grid[i].append(0)

                # adds the possible values to each i,j
                self.possibleValues[i].append([1,2,3,4,5,6,7,8,9])

        # gets first point to start of
        i = random.randint(0,8)
        j = random.randint(0,8)

        #iterates through the grid again to set the values
        self.grid = self.backtrack(random.randint(1,9), i,j, self.grid, self.possibleValues)

    # backtracking function to create the grid
    def backtrack(self, num, i , j, grid, possibleVals):
        newGrid = copy.deepcopy(grid)
        newPossibleVals = copy.deepcopy(possibleVals)

        # check each row
        for row in range(9):
            if grid[row][j] == num:
                return False

        #check each column
        for column in range(9):
            if grid[i][column] == num:
                return False

        # check which box it belongs to
        rowBox = (j) // 3
        columnBox = (i) // 3

        #check each box
        for row in range(1,4):
            for column in range(1,4):
                x = column+ 3*columnBox - 1
                y = row+ 3*rowBox - 1
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
            # created a working game
            return newGrid

        # we update all the other possible values

        # update each row
        for row in range(9):
            if row == i:
                continue
            if num in newPossibleVals[row][j]:
                newPossibleVals[row][j].remove(num)

        # update each column
        for column in range(9):
            if column == j:
                continue
            if num in newPossibleVals[i][column]:
                newPossibleVals[i][column].remove(num)

        # check which box it belongs to
        rowBox = (j) // 3
        columnBox = (i) // 3

        # update each box
        for row in range(1, 4):
            for column in range(1, 4):
                x = column + 3 * columnBox - 1
                y = row + 3 * rowBox - 1
                if x == i and y == j:
                    continue
                if num in newPossibleVals[x][y]:
                    newPossibleVals[x][y].remove(num)

        # one space has no more possible values left (base case)
        for I in range(9):
            for J in range(9):
                if len(newPossibleVals[I][J]) == 0 and newGrid[I][J] == 0:
                    return False

        # gets a new space
        # iterates through each position for least possible values
        Min = 9
        for I in range(9):
            for J in range(9):
                if (newGrid[I][J] != 0):
                    continue
                Min = min(Min, len(newPossibleVals[I][J]))

        newI = -1
        newJ = -1
        for I in range(9):
            for J in range(9):
                if len(newPossibleVals[I][J]) == Min and newGrid[I][J] == 0:
                    # found one of the elements with optimal size
                    newI = I
                    newJ = J
                    break

        # nums left to try for the spot
        nums = [1,2,3,4,5,6,7,8,9]

        # while there are still more options that can be tried for the current spot
        while(len(nums) != 0):
            newNumInd = random.randint(0,len(nums) - 1)
            newNum = nums[newNumInd]
            # reattain newInd because it updates every time
            # recursivly call function
            ret = self.backtrack(newNum, newI, newJ, newGrid, newPossibleVals)

            # the value we tried did not work
            if (ret == False):
                # we delete it from the nums options
                nums.pop(newNumInd)
            else:
                # here we got the base case which means the program is done
                return ret

        # no more options left to try so its done
        if len(nums) == 0:
            return False

