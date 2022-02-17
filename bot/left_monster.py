import pyautogui
import mouse
from time import sleep
import keyboard


def left_monster_action():
    mouse.move(488, 497)
    mouse.press(button="left")
    sleep(0.005)
    mouse.move(488, 680, duration=0.05)
    sleep(0.005)
    mouse.move(488, 880, duration=0.05)
    sleep(0.002)
    mouse.release(button="left")


def check_left_monster():
    pixel = pyautogui.pixel(488, 497)

    if pixel[0] in range(149, 161) and pixel[1] in range(221, 231):
        return True

    return False


if __name__ == "__main__":
    while keyboard.is_pressed("q") == False:
        print(pyautogui.pixel(488, 497))
