import pyautogui
import mouse
from time import sleep
import keyboard


def left_monster_action():
    mouse.move(484, 572)  # 803, 670
    mouse.press(button="left")
    sleep(0.01)
    pyautogui.moveTo(484, 812, 0.17)
    sleep(0.01)
    mouse.release(button="left")


def check_left_monster():
    pixel = pyautogui.pixel(467, 585)  # 803, 670

    if pixel[0] in range(90, 189) and pixel[1] in range(133, 221):
        left_monster_action()
        return True

    return False


if __name__ == "__main__":
    while keyboard.is_pressed("q") == False:
        print(pyautogui.pixel(467, 585))
