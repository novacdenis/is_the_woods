import pyautogui
import mouse
import keyboard
from time import sleep, time


def check_left_monster(update_poits=False):
    pixel = pyautogui.pixel(803, 670)

    if pixel[0] in range(154, 158) and pixel[1] in range(234, 238):
        if update_poits:
            update_poits(2)

        mouse.move(803, 670)
        mouse.press(button="left")
        sleep(0.01)
        pyautogui.moveTo(803, 910, 0.175)
        sleep(0.01)
        mouse.release(button="left")


if __name__ == "__main__":
    while keyboard.is_pressed("q") == False:
        time_start = time()
        check_left_monster()
        time_end = time()

        print(time_end - time_start)
