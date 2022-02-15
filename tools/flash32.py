from esptool import *
from time import sleep
import pyboard
from sys import platform

if platform == 'darwin':
    # MacOS
    from os import listdir
    devs = listdir("/dev/")
    for dev in devs:
        if "usb" in dev: PORT = "/dev/"+dev
else:
    # Linux
    PORT = "/dev/tty.usbserial-1420"

# factory "firmware_ULAB_LVGL_SPIRAM.bin" 
MPY = "../build/firmware_ESP32_ULAB_LVGL_SPIRAM_20220213-1722.bin"

# esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
# Erase
main(
    ["--port",PORT,
    "--chip", "esp32",
    "erase_flash"]
    )

# From then on program the firmware starting at address 0x1000:
# esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin
# Flash
main(
    ["--port",PORT,
    "--chip", "esp32",
    "--baud","460800",
    "write_flash",
    "-z", "0x1000", MPY]
)

sleep(2)
pyb = pyboard.Pyboard(PORT,115200)
pyb.enter_raw_repl()
print("Uploading boot.py")
pyb.fs_put("boot.py", "/etc/boot.py")
sleep(2)
print("Uploading main.py")
pyb.fs_put("main.py", "/etc/main.py")
sleep(2)
print("Uploading test.py")
pyb.fs_put("test.py", "/etc/test.py")
pyb.exit_raw_repl()
pyb.close()
print("Done")