import pyautogui
import time
import keyboard

mark = time.time()
while 1:
    if keyboard.is_pressed('space'):
        if time.time() - mark > 0.1:
            mark = time.time()
            pyautogui.moveTo(2741, 458)
            pyautogui.click()
            pyautogui.moveTo(2426, 669)
            pyautogui.click()
            print(1)
    elif keyboard.is_pressed('m'):
        if time.time() - mark > 0.1:
            mark = time.time()
            pyautogui.moveTo(2671, 360)
            pyautogui.click()
            time.sleep(2.3)
            pyautogui.moveTo(2833, 284)
            pyautogui.click()
            pyautogui.moveTo(2636, 538)
            pyautogui.click()
            pyautogui.moveTo(2676, 691)
            pyautogui.click()
            pyautogui.moveTo(2839, y=672)
            pyautogui.click()
            pyautogui.moveTo(1993, 1813)
            pyautogui.scroll(-10000)
            time.sleep(1.5)
            pyautogui.moveTo(2808, 1806)
            pyautogui.click()
            pyautogui.moveTo(1993, 1813)
            print(2)
