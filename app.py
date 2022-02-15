from time import sleep
import keyboard
import pyautogui
import mouse
import cv2 as cv
from bot.snowflake import find_snowflake_click_pos
from bot.middle_monster import check_middle_monster
from bot.left_monster import check_left_monster

LOW = 3
MEDIUM = 2
HIGH = 1

template = cv.imread("./templates/snowflake.png")
template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
template = cv.Canny(template, 50, 200)


class Game:
    score = 0
    max_score = 0

    def __init__(self):
        user_max_score = input("\nEnter max score: ")
        self.max_score = int(user_max_score)
        self.start_game()

    def detect_snowflake(self):
        snowflake = find_snowflake_click_pos(
            template,
            600,
            350,
            self.score,
        )

        if snowflake:
            self.score += 1

    def detect_monsters(self):
        middle_mon = check_middle_monster()
        left_mon = check_left_monster()

        if middle_mon:
            self.score += 2
        if left_mon:
            self.score += 2

    def start_game(self):
        print("\nPress 's' to start game")
        while keyboard.is_pressed("q") == False:
            if keyboard.read_key() == "s":
                print("\nGame started. Press 'q' to exit & stop game")
                self.analyze_screen()
                break

    def restart_game(self):
        mouse.move(1164, 885)
        sleep(0.1)
        mouse.press()
        sleep(0.1)
        mouse.release()
        sleep(3)

    def game_over(self):
        if self.score < self.max_score:
            print("\nGame over. Score", self.score)
            self.score = 0
            self.restart_game()
            self.analyze_screen()

    def analyze_screen(self):
        while keyboard.is_pressed("q") == False:
            pixel = pyautogui.pixel(1168, 937)

            if pixel[0] == 121 and pixel[1] == 2 and pixel[2] == 139:
                self.game_over()
                break

            if int(self.score) >= int(self.max_score):
                print("\nGame finished")
                break

            self.detect_snowflake()
            self.detect_monsters()


if __name__ == "__main__":
    game = Game()
