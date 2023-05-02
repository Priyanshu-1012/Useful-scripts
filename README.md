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
