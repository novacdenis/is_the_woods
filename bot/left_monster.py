import pyautogui
import mouse
import keyboard
from time import sleep


def left_monster_action():
    mouse.move(803, 670)
    mouse.press(button="left")
    sleep(0.01)
    pyautogui.moveTo(803, 910, 0.17)
    sleep(0.01)
    mouse.release(button="left")


def check_left_monster():
    pixel = pyautogui.pixel(803, 670)

    if pixel[0] in range(154, 158) and pixel[1] in range(234, 238):
        left_monster_action()
        return True

    return False
