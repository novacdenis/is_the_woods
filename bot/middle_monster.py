import pyautogui
import mouse
from time import sleep
import keyboard


def middle_monster_action():
    mouse.move(962, 733)
    mouse.click(button="left")
    sleep(0.01)


def check_middle_monster():
    pixel = pyautogui.pixel(962, 733)  # 1279, 917

    if pixel[0] in range(58, 79):  # 44, 52
        middle_monster_action()
        return True

    return False


if __name__ == "__main__":
    while keyboard.is_pressed("q") == False:
        print(pyautogui.pixel(962, 733))
