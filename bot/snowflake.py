from mss import mss
import cv2 as cv
import numpy as np
import imutils
import mouse
from time import sleep, time
import os

template = cv.imread(os.path.abspath("templates/snowflake.png"))
template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
template = cv.Canny(template, 50, 200)
H, W = template.shape[:2]

OFF_X, OFF_Y = 285, 176


def find_snowflake(screen):
    img = screen
    img = np.array(img)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edged = cv.Canny(gray, 50, 200)

    found = None

    for scale in np.linspace(0.2, 1.0, 2)[::-1]:
        resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])

        if resized.shape[0] < H or resized.shape[1] < W:
            break

        edged = cv.Canny(resized, 50, 200)
        result = cv.matchTemplate(edged, template, cv.TM_CCOEFF)
        (_, maxVal, _, maxLoc) = cv.minMaxLoc(result)

        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)

        if maxVal > 6225825:
            break

    if found[0] > 6225825:
        (_, maxLoc, r) = found
        (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
        (endX, endY) = (int((maxLoc[0] + W) * r), int((maxLoc[1] + H) * r))

        rect_width = (startX - endX) / 2
        rect_height = (startY - endY) / 2
        rect_x = startX + rect_width
        rect_y = startY + rect_height

        return {"x": rect_x, "y": rect_y}


def snowflake_action(args):
    """
    args[0] = x
    args[1] = y
    args[2] = sleep
    """
    mouse.move(args[0], args[1])
    mouse.click(button="left")

    if args[2] == True:
        sleep(0.03)


def find_snowflake_click_pos(game_start_time):
    with mss() as sct:
        current_screen = sct.grab(monitor=(241, 123, 1677, 1011))
        current_pos = find_snowflake(current_screen)

        current_played_time = time() - game_start_time

        if current_played_time > 270 and current_pos:
            snowflake_action((current_pos["x"] + OFF_X, current_pos["y"] + OFF_Y, True))
            return True

        if current_pos:
            sleep(0.009)
            next_screen = sct.grab(monitor=(241, 123, 1677, 1011))
            next_pos = find_snowflake(next_screen)

            if next_pos and next_pos["x"] == current_pos["x"]:
                snowflake_action(
                    (current_pos["x"] + OFF_X, current_pos["y"] + OFF_Y, False)
                )
                return True

        return False
