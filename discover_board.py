import pyautogui
import time


def find_left():
    """Determines the x, y position of the bottom left corners, along with the height of the minesweeper board"""
    screenshot = pyautogui.screenshot()
    width, height = pyautogui.size()

    pixelCount = 0
    firstLine = False
    for x in range(width):
        for y in range(height):
            target = screenshot.getpixel((x, y))
            if target == (189, 189, 189) and pixelCount >= 50:
                if firstLine is False:
                    firstLine = True
                else:
                    pyautogui.moveTo(x, y)
                    return (x, y), pixelCount
            if target == (123, 123, 123):
                pixelCount += 1
            else:
                pixelCount = 0
    return False


def find_Width(topLeft):
    """ Determines the width of the minesweeper board, which can be used to find the last two corners"""
    pixelCount = 0
    screenshot = pyautogui.screenshot()
    width = pyautogui.size()[0]

    for x in range(topLeft[0], width):
        target = screenshot.getpixel((x, topLeft[1]))
        if target == (123, 123, 123):
            pixelCount += 1
        else:
            return pixelCount


def find_start(x, y):
    """ Passed the x, y for the center of the board, go upwards to find the start button """
    screenshot = pyautogui.screenshot()
    pyautogui.moveTo(x, y)
    for y in range(y, 0, -15):
        target = screenshot.getpixel((x, y))
        if target == (255, 255, 0):
            pyautogui.moveTo(x, y)
            return x, y


def discover_board():
    """ Finds the x, y positions of the 4 corners of the game board, in addition to the start button"""
    bottomLeft, boardHeight = find_left()
    topLeft = bottomLeft[0], bottomLeft[1] - boardHeight

    boardWidth = find_Width(topLeft)

    bottomRight = bottomLeft[0] + boardWidth, bottomLeft[1]
    topRight = topLeft[0] + boardWidth, topLeft[1]

    startButton = find_start(((topLeft[0] + topRight[0]) // 2), topLeft[1])

    return topLeft, topRight, bottomLeft, bottomRight, boardWidth, boardHeight, startButton
