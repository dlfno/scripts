import pyautogui
import keyboard
import time
import sys
# import logging


def press(setkeys : list) -> None:
    state = True

    hotkeys = [keys[0] for keys in setkeys]

    while True:
        for i, hotkey in enumerate(hotkeys):
            if keyboard.is_pressed(hotkey):
                if state:
                    state = False
                    for key in keys[i][1:]:
                        if key != 'Mouse':
                            pyautogui.keyDown(key)
                        else:
                            pyautogui.mouseDown()
                else:
                    state = True
                    for key in keys[i][1:]:
                        if key != 'Mouse':
                            pyautogui.keyUp(key)
                        else:
                            pyautogui.mouseUp()


args = sys.argv[1:]
keys = []
lst = []

for arg in args:
    if arg[0] == '-':
        lst.insert(0, arg[1:])
        keys.append(lst)
        lst = []
    else:
        lst.append(arg)

try:
    for _ in range(30):
        press(keys)
except Exception as err:
    print(err)
