# Useful-scripts
python scripts I use to make my life easier :pinched_fingers:

if you have any suggestions...feel free to reach me!

## 1. Battery Percentage Notification 
I was unable to find this feature on my windows laptop...stop charging at 80% to maintain battery health or atleast notify me when battery percentage reach to 80%. So here's a simple script to notify me when it reach up to 80%.
make sure u got psutil, win10toast modules...to install it type... ```pip install psutil win10toast``` on elevated cmd.

```python

import psutil
from time import sleep
from win10toast import ToastNotifier

toaster = ToastNotifier()

while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged and percent >= 80:
        toaster.show_toast("Battery Alert", f"Battery level is {percent}%", duration=10)
        
    sleep(60)
```
make shortcut for the .py file... and paste the shortcut in startup folder usually its                                   ```C:\Users\username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup``` 
then go to its property and in Target field type *pythonw.exe* before the path of the script. 


## 2. CPU Temperature 
Just a simple script that displays CPU temperature in °C as a notification.

```python
import ctypes
import os
import subprocess
from win10toast import ToastNotifier

if not ctypes.windll.shell32.IsUserAnAdmin():
    script_path = os.path.abspath(__file__)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", script_path, None, 1)
    exit()

output = subprocess.check_output('wmic /namespace:\\\\root\\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature /value | findstr /r "^CurrentTemperature="', shell=True)

temp_str = output.decode().strip().split('=')[1]
temp_int = int(temp_str)

temp_celsius = round((temp_int / 10) - 273.15, 2)
# temp_fahren= round(((temp_int / 10) - 273.15)*9/5+32, 2)  #if you wanna use °F uncomment this line and comment out the above line


toaster = ToastNotifier()
toaster.show_toast("Temperature", f"{temp_celsius} °C", duration=3) 
# toaster.show_toast("Temperature", f"{temp_fahren} °F", duration=3)  #if you wanna use °F uncomment this line and comment out the above line
```

## 3. Automatic Google Meet
This script launches instant google meet , copies the link to clipboard, and then opens Whatsapp....(you know..to share the link)

Dependencies: ```pyautogui``` to install just type ```pip install pyautogui``` on yout terminal.

```python

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
```

## 4. Open a file or folder in VS code with a custom shortcut key

Here's  a python script that opens any file/folder in VS Code...i know its not the best..but it works for me...and its just a handy shortcut that i use a lot.

_Note:  **1.** I assigned the hotkey as ```Alt+V``` ..u may change it to your liking_

 
_**2.** I use the classic context menu and not the new win11 one...it wont work on the win 11 one._

![cmenu](https://user-images.githubusercontent.com/39450902/235765681-2ade4679-6ede-4d25-b457-8c514327a582.png)

```python

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
keyboard.add_hotkey('alt+v', on_sel)

keyboard.wait()
```
