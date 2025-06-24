import pyautogui
import re

# Controls clicking speed. 0.1 is default.
pyautogui.PAUSE = 0.1

# RBG Color Codes
# Empty Cell: 189, 189, 189
# Border : 255, 255, 255
# 1: 0, 0, 255
# 2: 0, 123, 0
# 3: 255, 0, 0
# 4: 0, 0, 123
# 5: 123, 0, 0
# 6: 0, 123, 123
# 7: 0, 0, 0
# 8: 123, 123, 123


def display_2D_grid(array):
    for x in range(len(array)):
        print(array[x])
    print()


def read_board(coordinateGameBoard, characterGameBoard):
    """
    Reads the RGB values are a given pixel coordinate to determine what exactly is on each given cell
    Is optimized to only read each cell once per game.
    """
    screenshot = pyautogui.screenshot()

    def read_cell(coordinates):
        count = 0
        for x in range(50):
            target = screenshot.getpixel((coordinates[0] - x, coordinates[1] - x))
            if target == (0, 0, 255):
                return "1"
            if target == (0, 123, 0):
                return "2"
            if target == (255, 0, 0):
                return "3"
            if target == (0, 0, 123):
                return "4"
            if target == (123, 0, 0):
                return "5"
            if target == (0, 123, 123):
                return "6"
            if target == (0, 0, 0):
                return "7"
            if target == (123, 123, 123) and count < 5:
                return "8"
            if target == (255, 255, 255):
                return "?"
            count += 1
        return " "

    for column in range(len(coordinateGameBoard)):
        for row in range(len(coordinateGameBoard[0])):
            if characterGameBoard[column][row] == "?" or characterGameBoard[column][row] == "!":
                characterGameBoard[column][row] = read_cell(coordinateGameBoard[column][row])


def find_moves(coordinateGameBoard, characterGameBoard):
    """
    Cycles through all cells on a game board and clicks or flags every cell with enough information to determine
    if it is safe or not. If no move is made, it will resort to guessing.
    Returns False is the game is ongoing. Otherwise, return True is game is over.
    """
    def find_surrounding_cells(column, row):
        """
        Returns an array of x, y, coordinates of cells surrounding a passed number cell with possible mines around it.
        This means 8 cells maximum are checked or 3 minimum if the given cell is in a corner
        """
        blankCells = []
        mineCells = []
        for y in range(column - 1, column + 2):
            for x in range(row - 1, row + 2):
                if (y < 0 or x < 0 or y > len(characterGameBoard) - 1 or x > len(characterGameBoard[0]) - 1) or (y == column and x == row):
                    continue
                if characterGameBoard[y][x] == '?':
                    blankCells.append((y, x))
                if characterGameBoard[y][x] == 'M':
                    mineCells.append((y, x))
        return blankCells, mineCells

    madeAction = False

    # 1 - 9 value represent their corresponding integers on the Minesweeper board
    # ? = Unclicked cell
    # ! = Clicked cell that needs to be checked to see which integer is under it
    # M = Mine, these are flagged to not be clicked
    for column in range(len(characterGameBoard)):
        for row in range(len(characterGameBoard[0])):
            if bool(re.search(r'[1-9]', characterGameBoard[column][row])) is True:
                surroundingBlankCells, surroundingMines = find_surrounding_cells(column, row)
                if int(characterGameBoard[column][row]) == len(surroundingBlankCells) + len(surroundingMines):
                    # A mine is confirmed in surrounding cells.
                    # We mark it on our gameBoard in addition to clicking its spot on the screen
                    for x in range(len(surroundingBlankCells)):
                        indexPosition = surroundingBlankCells[x]
                        characterGameBoard[indexPosition[0]][indexPosition[1]] = 'M'
                        # Right-clicking to flag mines is just for show. Can disable to speed up execution
                        pyautogui.rightClick(coordinateGameBoard[indexPosition[0]][indexPosition[1]])
                        madeAction = True
                elif len(surroundingBlankCells) == 0:
                    # If there are no cells to click surrounding a number, as far as the program is concerned we can
                    # ignore it from now on. Setting it to a different value to not waste computation time later
                    characterGameBoard[column][row] = '-'
                if len(surroundingMines) == int(characterGameBoard[column][row]) and len(surroundingBlankCells) > 0:
                    for x in range(len(surroundingBlankCells)):
                        indexPosition = surroundingBlankCells[x]
                        characterGameBoard[indexPosition[0]][indexPosition[1]] = '!'
                        pyautogui.click(coordinateGameBoard[indexPosition[0]][indexPosition[1]])
                        madeAction = True
    if madeAction is False:
        # If we reach this point, the code hasn't made a move this round, so either two events have happened.
        #  1. the program couldn't find a guaranteed click, and we have to resort to a guess
        #  This can happen often in Minesweeper games. There is no way to guarantee a win in every game.
        #  2. It hasn't made a move since there are no more to make. Meaning the game is over and you won.
        for column in range(len(characterGameBoard)):
            for row in range(len(characterGameBoard[0])):
                if bool(re.search(r'[1-9]', characterGameBoard[column][row])) is True:
                    surroundingBlankCells, surroundingMines = find_surrounding_cells(column, row)
                    if len(surroundingBlankCells) > 0:
                        # We tell the program to click on the first non-clicked cell next to a number cell
                        pyautogui.click(coordinateGameBoard[surroundingBlankCells[0][0]][surroundingBlankCells[0][1]])
                        return False
        print("You won!!!")
        return True
    else:
        return False


def play_board(coordinateGameBoard, start):
    characterGameBoard = [["?" for _ in range(len(coordinateGameBoard))] for _ in range(len(coordinateGameBoard[0]))]

    # while True:
    for x in range(10):
        read_board(coordinateGameBoard, characterGameBoard)
        if find_moves(coordinateGameBoard, characterGameBoard) is False:
            continue
        else:
            return True
