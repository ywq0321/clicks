import pyautogui
import time
import keyboard

x = 1920
y = 1080

mark = time.time()
while 1:
    if keyboard.is_pressed('space'):
        if time.time() - mark > 0.1:
            mark = time.time()
            pyautogui.moveTo(int(0.625*x*2741/3000), int(0.625*y*458/2000))
            pyautogui.click()
            pyautogui.moveTo(int(0.625*x*2426/3000), int(0.625*y*669/3000))
            pyautogui.click()
            print(1)
    elif keyboard.is_pressed('m'):
        if time.time() - mark > 0.1:
            mark = time.time()
            pyautogui.moveTo(int(0.625*x*2671/3000), int(0.625*y*360/3000))
            pyautogui.click()
            time.sleep(2.3)
            pyautogui.moveTo(int(0.625*x*2833/3000), int(0.625*y*284/3000))
            pyautogui.click()
            pyautogui.moveTo(int(0.625*x*2636/3000), int(0.625*y*538/3000))
            pyautogui.click()
            pyautogui.moveTo(int(0.625*x*2676/3000), int(0.625*y*691/3000))
            pyautogui.click()
            pyautogui.moveTo(int(0.625*x*2839/3000), int(0.625*y*672/3000))
            pyautogui.click()
            pyautogui.moveTo(int(0.625*x*1993/3000), int(0.625*y*1813/3000))
            pyautogui.scroll(-10000)
            time.sleep(1.5)
            pyautogui.moveTo(int(0.625*x*2808/3000), int(0.625*y*1806/3000))
            pyautogui.click()
            pyautogui.moveTo(int(0.625*x*1993/3000), int(0.625*y*1813/3000))
            print(2)
