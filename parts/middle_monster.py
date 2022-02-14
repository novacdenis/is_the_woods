import pyautogui
from time import sleep
import mouse
import keyboard


def check_middle_monster(update_poits=False):
    pixel = pyautogui.pixel(1279, 917)

    if pixel[0] in range(44, 52):
        if update_poits:
            update_poits(2)

        mouse.move(1279, 917)
        mouse.click(button="left")
        sleep(0.01)


if __name__ == "__main__":
    while keyboard.is_pressed("q") == False:
        if keyboard.is_pressed("s"):
            print(pyautogui.pixel(1279, 917))
