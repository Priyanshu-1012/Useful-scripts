# Useful-scripts
python scripts I use to make my life easier

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

toaster = ToastNotifier()
toaster.show_toast("Temperature", f"{temp_celsius} °C", duration=3)

```
