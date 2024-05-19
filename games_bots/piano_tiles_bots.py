import random
import keyboard
import time
import pyautogui
import win32api
import win32con
import numpy as np

# tiles_Position_array = np.array([377, 539], [475, 368], [560, 388], [643, 283])
# tiles_Color_array = np.arrays([(22, 45, 86)], [(21, 47, 86)], [(23, 49, 86)] ,[(23, 39, 86)]

#view location of the set click points
pyautogui.displayMousePosition()

"""Line1 and line2 are set up points that are used to trigger the click
function"""

line1 = [(216, 249),(310, 247),(388, 248), (452, 244)]
line2 = [(221, 507), (300, 517), (382, 516), (453, 504)]

# click function with timer added for screen adjustment
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)# this pauses the script for 0.01 sec
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def main():
    try:
        while keyboard.is_pressed('q') == False:
            for x,y in line1:
                if pyautogui.pixel(x,y)[2] == 86:
                    click(x,y)

    except Exception as e:
        print(f"An error has occured: {e}")

if __name__ == "__main__":
    main()
