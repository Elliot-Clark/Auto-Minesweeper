import pyautogui
import re
import time

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


def read_board(coordinateGameBoard, characterGameBoard):
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
            if characterGameBoard[column][row] == "?":
                characterGameBoard[column][row] = read_cell(coordinateGameBoard[column][row])


def play_board(coordinateGameBoard, start):
    display_2D_grid(coordinateGameBoard)
    characterGameBoard = [["?" for _ in range(len(coordinateGameBoard))] for _ in range(len(coordinateGameBoard[0]))]

    # while True:
    read_board(coordinateGameBoard, characterGameBoard)
    display_2D_grid(characterGameBoard)
