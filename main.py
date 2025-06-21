import time
import keyboard
import pyautogui
import win32api
import win32con
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

    # gameBoard, startButton = discover_board()
    # display_2D_grid(gameBoard)
    # print(startButton)

    # 300% zoom
    tmpBoard = [
        [(1069, 575), (1141, 575), (1214, 575), (1286, 575), (1359, 575), (1431, 575), (1504, 575), (1576, 575),
         (1649, 575)],
        [(1069, 647), (1141, 647), (1214, 647), (1286, 647), (1359, 647), (1431, 647), (1504, 647), (1576, 647), (
            1649, 647)],
        [(1069, 720), (1141, 720), (1214, 720), (1286, 720), (1359, 720), (1431, 720), (1504, 720), (1576, 720), (
            1649, 720)],
        [(1069, 793), (1141, 793), (1214, 793), (1286, 793), (1359, 793), (1431, 793), (1504, 793), (1576, 793), (
            1649, 793)],
        [(1069, 866), (1141, 866), (1214, 866), (1286, 866), (1359, 866), (1431, 866), (1504, 866), (1576, 866), (
            1649, 866)],
        [(1069, 938), (1141, 938), (1214, 938), (1286, 938), (1359, 938), (1431, 938), (1504, 938), (1576, 938), (
            1649, 938)],
        [(1069, 1011), (1141, 1011), (1214, 1011), (1286, 1011), (1359, 1011), (1431, 1011), (1504, 1011), (
            1576, 1011), (1649, 1011)],
        [(1069, 1084), (1141, 1084), (1214, 1084), (1286, 1084), (1359, 1084), (1431, 1084), (1504, 1084), (
            1576, 1084), (1649, 1084)],
        [(1069, 1157), (1141, 1157), (1214, 1157), (1286, 1157), (1359, 1157), (1431, 1157), (1504, 1157), (
            1576, 1157), (1649, 1157)]
    ]
    tmpStart = (763, 642)

    # Now that we have all the information, we can start the game.
    start_game(tmpStart, tmpBoard)

    # And with the game started, we can start reading what is on the cells and playing the game in play_board.py
    play_board(tmpBoard, tmpStart)


keyboard.add_hotkey('=', auto_Minesweeper)
keyboard.add_hotkey('-', print_rgb)

print("Running Program")
keyboard.wait('esc')
