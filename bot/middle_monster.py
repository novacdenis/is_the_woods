import pyautogui
import mouse
from time import sleep
import keyboard


def middle_monster_action():
    mouse.move(960, 742)
    mouse.click(button="left")
    sleep(0.001)


def check_middle_monster():
    pixel = pyautogui.pixel(960, 742)

    if pixel[0] in range(38, 47):
        return True

    return False


if __name__ == "__main__":
    while keyboard.is_pressed("q") == False:
        if keyboard.is_pressed("s"):
            while keyboard.is_pressed("r") == False:
                pixel = pyautogui.pixel(960, 742)
                print(pixel)
            break
