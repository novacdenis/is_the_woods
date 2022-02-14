from time import sleep, time
import cv2 as cv
import keyboard
import pyautogui
import mouse
from bot.snowflake import find_snowflake_click_pos
from bot.middle_monster import check_middle_monster
from bot.left_monster import check_left_monster


MAX_POINTS = 950
POINTS = 0


template = cv.imread("./templates/test1.png")
template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
template = cv.Canny(template, 50, 200)


def update_poits(n):
    global POINTS
    POINTS += n


def game_over():
    global POINTS

    if POINTS < MAX_POINTS:
        print("GAME OVER")
        mouse.move(1164, 883)
        sleep(0.1)
        mouse.press(button="left")
        sleep(0.1)
        mouse.release(button="left")
        sleep(5)
        POINTS = 0
        start_game()
    else:
        print("MAX POINTS EXCEEDED")


def start_game():
    while keyboard.is_pressed("q") == False:
        pixel = pyautogui.pixel(1168, 937)

        if POINTS > MAX_POINTS:
            game_over()
            break

        if pixel[0] == 121 and pixel[1] == 2 and pixel[2] == 139:
            print(POINTS)
            game_over()
            break

        find_snowflake_click_pos(
            template,
            600,
            350,
            update_poits,
            POINTS,
        )

        check_middle_monster(update_poits)

        find_snowflake_click_pos(
            template,
            600,
            350,
            update_poits,
            POINTS,
        )

        check_left_monster(update_poits)


if __name__ == "__main__":
    while keyboard.is_pressed("q") == False:
        if keyboard.read_key() == "s":
            start_game()
            break
