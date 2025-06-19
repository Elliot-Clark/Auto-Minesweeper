import time
import keyboard
import pyautogui
import win32api
import win32con
from discover_board import discover_board
from discover_tiles import discover_tiles

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


def click(x, y):
    pyautogui.moveTo(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.05)


def start_game():

    topLeft, topRight, bottomLeft, bottomRight, boardWidth, boardHeight, startButton = discover_board()
    print(topLeft, topRight, bottomLeft, bottomRight, boardWidth, boardHeight, startButton)

    heightTileCount, widthTileCount = discover_tiles(topLeft, boardHeight, boardWidth)
    print("The Minesweeper board is", heightTileCount, "by", widthTileCount)


keyboard.add_hotkey('=', start_game)
keyboard.add_hotkey('-', print_cursor_position)

print("Running Program")
keyboard.wait('esc')

