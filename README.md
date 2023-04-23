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
