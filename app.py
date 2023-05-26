import os
from time import sleep, time
import keyboard
import pyautogui
import mouse
import json
from utils import clear_console
from bot.snowflake import find_snowflake_click_pos
from bot.middle_monster import check_middle_monster, middle_monster_action
from bot.left_monster import check_left_monster, left_monster_action

LOW = 3
MEDIUM = 2
HIGH = 1
ULTRA = 0


class Game:
    actions = []
    start_time = None
    loop_average_time = 0
    loops_count = 0

    def __init__(self):
        self.start_game()

    def detect_snowflake(self):
        find_snowflake_click_pos(self.start_time)

    def detect_monsters(self):
        middle_mon = check_middle_monster()
        left_mon = check_left_monster()

        if middle_mon:
            self.actions.append({"priority": LOW, "fn": middle_monster_action})
        if left_mon:
            self.actions.append({"priority": MEDIUM, "fn": left_monster_action})

    def start_game(self):
        clear_console()

        print("Press 's' to start game or press 'q' to exit")

        while keyboard.is_pressed("q") == False:
            if keyboard.read_key() == "s":
                print("\nGame started. Press 'q' to exit & stop game")
                self.analyze_screen()
                break

    def restart_game(self):
        mouse.move(849, 706)
        sleep(0.1)
        mouse.press()
        sleep(0.1)
        mouse.release()
        sleep(3)

    def game_over(self):
        end_time = time()

        played_time = end_time - self.start_time
        loop_average_time = self.loop_average_time / self.loops_count

        if played_time > 200:
            self.update_report_file(played_time, loop_average_time)

        print("\nPlayed Time: {}s".format(played_time))
        print("Loop average time: {}s".format(loop_average_time))

        if played_time < 300:
            self.restart_game()
        else:
            print("\nPress 'r' to restart game or press 'q' to exit")

            while keyboard.is_pressed("q") == False:
                if keyboard.is_pressed("r"):
                    self.restart_game()
                    self.analyze_screen()

    def start_actions(self):
        sorted_action = sorted(self.actions, key=lambda i: i["priority"])

        for action in sorted_action:
            action["fn"]()

        self.actions.clear()

    def update_report_file(self, total, loop):
        with open("report.json", "r") as report_file:
            data = json.load(report_file)

        data.append({"total": total, "loop": loop})

        with open("report.json", "w") as report_file:
            json.dump(data, report_file)

    def analyze_screen(self):
        self.start_time = time()
        self.loops_count = 0
        self.loop_average_time = 0

        while True:
            loop_start_time = time()

            if keyboard.is_pressed("q"):
                self.game_over()
                break

            if loop_start_time - self.start_time > 345:
                print("I think this is enough")
                break

            loop_start_time = time()

            pixel = pyautogui.pixel(846, 758)

            if pixel[0] == 121 and pixel[1] == 1 and pixel[2] == 139:
                self.game_over()
                break

            self.detect_snowflake()
            self.detect_monsters()
            self.detect_snowflake()
            self.start_actions()

            loop_end_time = time()

            self.loop_average_time += loop_end_time - loop_start_time
            self.loops_count += 1


if __name__ == "__main__":
    game = Game()
