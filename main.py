import keyboard
import pyautogui
from discover_board import discover_board
from play_board import play_board


# Start button RGB: 255, 255, 0
# Border RGB: 189, 189, 189
# Game border RBG: 123, 123, 123


def print_cursor_position():
    x, y = pyautogui.position()
    print(f"Cursor Position: ({x}, {y})")
    return x, y


def print_rgb():
    x, y = pyautogui.position()
    r, g, b = pyautogui.pixel(x, y)
    print(f"RGB Values: {r}, {g}, {b}")


def start_game(gameBoard, startButton):
    """ Clicks the smile face to possibly reset the board, then clicks the middle of the board to start the game"""
    pyautogui.click(startButton)
    middleRow = len(gameBoard) // 2
    middleCol = len(gameBoard[0]) // 2
    pyautogui.click(gameBoard[middleRow][middleCol])


gameBoard = False
startButton = False


def auto_Minesweeper():
    """Main Function of this program. Auto plays Minesweeper upon pressing the hotkey with the gameboard on screen"""

    # To autoplay Minesweeper we first need to know everything about the board.
    # Where is it on the screen, how many rows and columns there. Where to click to start and pick any given cell.
    # This is all determined using pyautogui and screen reading in the discover_board.py file
    # What we need from it is mostly the x, y pixel coordinates on your screen for every cell on the Minesweeper board
    # This information only needs to be determined once on initialization, and won't run again if there are repeat plays
    global gameBoard, startButton
    if gameBoard is False:
        gameBoard, startButton = discover_board()

    # Now that we have all the information, we can start the game.
    start_game(gameBoard, startButton)

    # And with the game started, we can start reading what is on the cells and playing the game in play_board.py
    play_board(gameBoard)


keyboard.add_hotkey('=', auto_Minesweeper)
print("Running Program. Press the = key to play. Press Esc to Exit.")
keyboard.wait('esc')
