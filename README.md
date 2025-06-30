# Auto Minesweeper
Auto Minesweeper is a Python project that utilizes pyautogui to both read your screen and click and precise locations to complete game of Minesweeper for you. 
It has been designed to work with any size of Minesweeper, at any location on your screen.
Due to the nature of Minesweeper, it is not possible to guarantee a win every game as soon rounds will leave you no choice but to resort to guessing. 

To use, simply clone the files of this repository, install the required packages, and run: **main.py**.
With it running ensure you have the Minesweeper game active on your screen and press the **=** key. To stop the program you can either kill the process from your IDE, or hit the **Esc** key.
If at any point you would like to force the execution of the program to stop while it has control over your mouse, quickly move the cursor to one of the corners of your screen to activate a fail-safe stop.

You can test it out here: [Minesweeper Online](https://minesweeperonline.com/#beginner)

## Altering Execution Speed

At the top of the **play_board.py** file is a setting for: **pyautogui.PAUSE**
This controls the time delay between each click pyautogui performs and can be changed to your desire. 
For reference 0.1 speed is demonstrated on the beginner and intermediate levels in the animated gif below while 0.01 speed is used on the expert level.
Keep in mind, pyautogui clicking at 0.01 will make it harder to trigger a fail-safe stop.

![Auto Minesweeper being used on three difficulties of Minesweeper](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmlmdHVvYzd4NXlodHd1aDM2YzRpc2pncmJkbjRnanZtdnp6bzBycCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TeYY3hh41kxCadW790/giphy.gif)

