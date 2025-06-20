import time
import keyboard
import pyautogui
import win32api
import win32con
from discover_board import discover_board

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


def click(pixelCoordinates):
    pyautogui.moveTo(pixelCoordinates[0], pixelCoordinates[1])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.05)


def display_2D_grid(array):
    for x in range(len(array)):
        print(array[x])


def start_game(startButton, gameBoard):
    """ Clicks the smile face to possibly reset the board, then clicks the middle of the board to start the game"""
    click(startButton)
    middleRow = len(gameBoard) // 2
    middleCol = len(gameBoard[0]) // 2
    click(gameBoard[middleRow][middleCol])


def auto_Minesweeper():
    """"""

    # To autoplay Minesweeper we first need to know everything about the board.
    # Where is it on the screen, how many rows and columns there. Where to click to start and pick any given cell.
    # This is all determined using pyautogui and screen reading in the discover_board.py file
    # What we need from it is mostly the x, y pixel coordinates on your screen for every cell on the Minesweeper board
    # This information only needs to be determined once on initialization, and won't run again on repeat plays
    gameBoard, startButton = discover_board()
    display_2D_grid(gameBoard)
    print(startButton)

    # Now that we have all the information, we can start the game.
    start_game(startButton, gameBoard)


keyboard.add_hotkey('=', auto_Minesweeper)
# keyboard.add_hotkey('-', print_cursor_position)

print("Running Program")
keyboard.wait('esc')

