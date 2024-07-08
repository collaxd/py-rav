from pynput import keyboard
import pyautogui
import random
import time

INFUSE_SPOTS = [
    (80, 513),
    (138, 451),
    (138, 515),
    (203, 515),
    (203, 455),
    (268, 453),
    (270, 520),
]

SPOT_OFFSET_MAX = 5
MIN_DELAY = 0.250
MAX_DELAY = 0.500


def random_delay():
    time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))


def random_click(coords, click_count=1):
    x, y = coords
    offset_x = random.randint(-SPOT_OFFSET_MAX, SPOT_OFFSET_MAX)
    offset_y = random.randint(-SPOT_OFFSET_MAX, SPOT_OFFSET_MAX)
    pyautogui.moveTo(x + offset_x, y + offset_y)
    pyautogui.click(x + offset_x, y + offset_y, clicks=click_count)
    random_delay()


def infuse():
    random_click((737, 722))
    random_click((1239, 567))


def select_infusioned_item():
    random_click((79, 455), 2)


def main():
    MAX_COUNT = 50
    while MAX_COUNT > 0:
        random.shuffle(INFUSE_SPOTS)
        for i in range(4):
            random_click(INFUSE_SPOTS[i], 2)
            MAX_COUNT -= 1
        infuse()


def on_press(key):
    if key == keyboard.Key.f1:
        # print(pyautogui.position())
        main()

    if key == keyboard.Key.esc:
        # Stop listener
        return False


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
