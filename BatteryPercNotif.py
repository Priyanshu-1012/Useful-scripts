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
