from mss import mss
import cv2 as cv
import numpy as np
import imutils
import mouse
from time import sleep


def find_snowflake(screen, template, w, h):
    img = screen
    img = np.array(img)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edged = cv.Canny(gray, 50, 200)

    found = None

    for scale in np.linspace(0.2, 1.0, 2)[::-1]:
        resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])

        if resized.shape[0] < h or resized.shape[1] < w:
            break

        edged = cv.Canny(resized, 50, 200)
        result = cv.matchTemplate(edged, template, cv.TM_CCOEFF)
        (_, maxVal, _, maxLoc) = cv.minMaxLoc(result)

        # print(f"[{count}, {maxVal}],")

        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)

        if maxVal > 6225825:
            break

    if found[0] > 6225825:
        (_, maxLoc, r) = found
        (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
        (endX, endY) = (int((maxLoc[0] + w) * r), int((maxLoc[1] + h) * r))

        rect_width = (startX - endX) / 2
        rect_height = (startY - endY) / 2
        rect_x = startX + rect_width
        rect_y = startY + rect_height

        return {"x": rect_x, "y": rect_y}


def action(x, y, slp=False):
    mouse.move(x, y)
    mouse.click(button="left")
    sleep(0.01)

    if slp == True:
        sleep(0.02)


def find_snowflake_click_pos(template, offsetX, offsetY, update_poits, points):
    (snowflake_h, snowflake_w) = template.shape[:2]

    with mss() as sct:
        current_screen = sct.grab(monitor=(560, 300, 2000, 1200))
        current_pos = find_snowflake(current_screen, template, snowflake_w, snowflake_h)

        if points > 800 and current_pos:
            action(current_pos["x"] + offsetX, current_pos["y"] + offsetY, slp=True)

        if current_pos:
            sleep(0.009)
            next_screen = sct.grab(monitor=(560, 300, 2000, 1200))
            next_pos = find_snowflake(next_screen, template, snowflake_w, snowflake_h)

            if next_pos and next_pos["x"] == current_pos["x"]:
                update_poits(1)
                action(current_pos["x"] + offsetX, current_pos["y"] + offsetY)