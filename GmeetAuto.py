import os
import time
import pyautogui

wapp_path="C:\\WhatsApp - Shortcut.lnk"  #change Whatsapp path according to your system
os.startfile("msedge.exe")               #this one too
time.sleep(0.5) 
pyautogui.typewrite("https://meet.google.com/")
time.sleep(0.05)
pyautogui.press('enter')
time.sleep(5)
pyautogui.press('space')
time.sleep(0.5)
pyautogui.press('down')
time.sleep(0.5)
pyautogui.press('space')
time.sleep(8)
for i in range(20):
    pyautogui.press('tab')
    time.sleep(0.01)
pyautogui.press('space')

os.startfile(wapp_path)