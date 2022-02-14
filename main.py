import cv2 as cv
import keyboard
import pyautogui
import mouse
from time import sleep
from bot.snowflake import find_snowflake_click_pos
from bot.middle_monster import check_middle_monster
from bot.left_monster import check_left_monster


MAX_POINTS = 962
POINTS = 0


template = cv.imread("./templates/snowflake.png")
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


def task1():
    find_snowflake_click_pos(
        template,
        600,
        350,
        update_poits,
        POINTS,
    )


def task2():
    check_middle_monster(update_poits)
    check_left_monster(update_poits)


def start_game():
    while keyboard.is_pressed("q") == False:
        pixel = pyautogui.pixel(1168, 937)

        if POINTS > MAX_POINTS:
            game_over()
            break

        if pixel[0] == 121 and pixel[1] == 2 and pixel[2] == 139:
            game_over()
            break

        task1()
        task2()


if __name__ == "__main__":
    while keyboard.is_pressed("q") == False:
        if keyboard.read_key() == "s":
            start_game()
            break
