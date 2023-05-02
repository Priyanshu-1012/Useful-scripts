import keyboard
import pyautogui
import time
import pyperclip
import os

def on_sel():
    time.sleep(0.5)
    pyautogui.rightClick()
    time.sleep(0.5)
    keyboard.press('a')
    keyboard.release('a')
    time.sleep(0.5)
    clipboard_value = pyperclip.paste()
    os.system(f'cmd /c "code {clipboard_value}"')

# add hotkey listener for Alt+V
keyboard.add_hotkey('alt+b', on_sel)

keyboard.wait()



