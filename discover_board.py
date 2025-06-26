import pyautogui


def display_2D_grid(array):
    """ Displays arrays in a grid format. Used for visualization and testing purposes only."""
    for i in range(len(array)):
        print(array[i])
    print()


def find_leftSide():
    """
    Determines the x, y position of the bottom left corner, along with the height of the minesweeper board
    This works by searching every pixel on the screen until a vertical line with an exact grey color is found
    """
    screenshot = pyautogui.screenshot()
    screenWidth, screenHeight = pyautogui.size()

    pixelCount = 0
    firstLine = False
    for x in range(screenWidth):
        for y in range(screenHeight):
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
    """
    Determines the width of the minesweeper board, which can be used to find the last two corners
    This works by going across the horizontal grey line until a new color signals the line has ended
    """
    pixelCount = 0
    screenshot = pyautogui.screenshot()
    screenWidth = pyautogui.size()[0]

    for x in range(topLeft[0], screenWidth):
        target = screenshot.getpixel((x, topLeft[1]))
        if target == (123, 123, 123):
            pixelCount += 1
        else:
            return pixelCount


def find_start(x, y):
    """ Passed the x, y for the center of the board, go upwards to find the start button """
    screenshot = pyautogui.screenshot()
    for y in range(y, 0, -15):
        target = screenshot.getpixel((x, y))
        if target == (255, 255, 0):
            return x, y


def discover_tiles(topLeft, boardWidth, boardHeight):
    """
    Returns how many tiles tall and wide the game board is
    This works since every cell in the game has a white border around it.
    We simply count how many times we come across that as we read every pixel up/across in the game board's dimensions
    """
    # 5% of the respective measurements positions us into a cell. We don't want to measure from the exact top
    startingWidthCountPosition = int(topLeft[1] + (.05 * boardHeight))
    startingHeightCountPosition = int(topLeft[0] + (.05 * boardWidth))

    screenshot = pyautogui.screenshot()
    widthTileCount = 0
    heightTileCount = 0
    borderEnd = True

    # Finding Vertical Cell Count
    for y in range(topLeft[1], topLeft[1] + boardHeight - 10, 4):
        target = screenshot.getpixel((startingHeightCountPosition, y))
        if target == (255, 255, 255) and borderEnd is True:
            heightTileCount += 1
            borderEnd = False
        if target != (255, 255, 255):
            borderEnd = True

    borderEnd = True

    # Finding Horizontal Cell Count
    for x in range(topLeft[0], topLeft[0] + boardWidth - 10, 4):
        target = screenshot.getpixel((x, startingWidthCountPosition))
        if target == (255, 255, 255) and borderEnd is True:
            widthTileCount += 1
            borderEnd = False
        if target != (255, 255, 255):
            borderEnd = True

    print("The Minesweeper board is", heightTileCount, "by", widthTileCount)
    return produce_grid(topLeft, boardHeight, boardWidth, heightTileCount, widthTileCount)


def produce_grid(topLeft, boardHeight, boardWidth, heightTileCount, widthTileCount):
    """
    At this point we know the pixel position, height/width and number of tiles, so we can calculate a 2D array
    grid containing the horizontal and vertical center of every cell on the Minesweeper board.
    This information will be used to determine where to click and what exactly is on each cell going forward
    """
    gameBoard = [[0 for _ in range(widthTileCount)] for _ in range(heightTileCount)]
    offsetX = int(boardWidth * 1 / widthTileCount * .5)
    offsetY = int(boardHeight * 1 / heightTileCount * .5)

    for y in range(heightTileCount):
        for x in range(widthTileCount):
            gameBoard[y][x] = (
                topLeft[0] + int(boardWidth * x/widthTileCount) + offsetX,
                topLeft[1] + int(boardHeight * y/heightTileCount) + offsetY
            )
    return gameBoard


def discover_board():
    """
    Reads and determines every aspect of the Minesweeper board you are playing with
    Returns a 2D array with the x, y pixel coordinates of the center of every tile on the board on your screen
    """

    # Finds the xy positions of 3 corners of the game board, board dimensions, in addition to the start button location
    bottomLeft, boardHeight = find_leftSide()
    topLeft = bottomLeft[0], bottomLeft[1] - boardHeight
    boardWidth = find_Width(topLeft)
    topRight = topLeft[0] + boardWidth, topLeft[1]
    startButton = find_start(((topLeft[0] + topRight[0]) // 2), topLeft[1])

    # With that information we go on to find how many columns and rows the game board has
    # In addition we also find the center of every single cell
    gameBoard = discover_tiles(topLeft, boardWidth, boardHeight)

    return gameBoard, startButton
