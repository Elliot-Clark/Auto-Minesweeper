import pyautogui
import time


def discover_tiles(topLeft, boardWidth, boardHeight):
    """Returns how many tiles tall and wide the game board is"""
    # 5% of the respective measurements positions us into a cell. We don't want to measure from the exact top
    startingWidthCountPosition = int(topLeft[1] + (.05 * boardHeight))
    startingHeightCountPosition = int(topLeft[0] + (.05 * boardWidth))

    screenshot = pyautogui.screenshot()
    widthTileCount = 0
    heightTileCount = 0
    lineEnd = True

    # Finding Vertical Cell Count
    for y in range(topLeft[1], topLeft[1] + boardHeight - 10, 4):
        target = screenshot.getpixel((startingHeightCountPosition, y))
        if target == (255, 255, 255) and lineEnd is True:
            heightTileCount += 1
            lineEnd = False
            pyautogui.moveTo((startingHeightCountPosition, y))
            time.sleep(.25)
        if target != (255, 255, 255):
            lineEnd = True

    lineEnd = True

    # Finding Horizontal Cell Count
    for x in range(topLeft[0], topLeft[0] + boardWidth - 10, 4):
        target = screenshot.getpixel((x, startingWidthCountPosition))
        if target == (255, 255, 255) and lineEnd is True:
            widthTileCount += 1
            lineEnd = False
        if target != (255, 255, 255):
            lineEnd = True

    return heightTileCount, widthTileCount
