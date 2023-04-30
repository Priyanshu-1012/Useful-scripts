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
