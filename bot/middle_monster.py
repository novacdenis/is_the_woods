import pyautogui
import mouse
from time import sleep


def middle_monster_action():
    mouse.move(1279, 917)
    mouse.click(button="left")
    sleep(0.01)


def check_middle_monster():
    pixel = pyautogui.pixel(1279, 917)

    if pixel[0] in range(44, 52):
        middle_monster_action()
        return True

    return False
