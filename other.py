import keyboard
import pyautogui
from parts.middle_monster import check_middle_monster
from parts.left_monster import check_left_monster


def start_game():
    while keyboard.is_pressed("q") == False:
        pixel = pyautogui.pixel(1279, 917)

        if pixel[0] == 28 and pixel[1] == 13 and pixel[2] == 29:
            break

        check_middle_monster()
        check_left_monster()


if __name__ == "__main__":
    while keyboard.is_pressed("q") == False:
        if keyboard.read_key() == "s":
            start_game()
            break
