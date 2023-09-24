# Experimental firmware micropthon v1.20 and LVGL 9.0
This is the newest lv_micropython firmware compiled for LMS-ESP32. 

## micropython v1.20
See [release notes v1.20](https://github.com/micropython/micropython/releases) for changes. 
Nice additions are:
- addition of hex/fromhex methods to bytes/memoryview/bytearray
- support for mip packages which allows to install apckages straight from github e.g.

```
# wifi should be configured and active
import mip
mip.install("github:antonvh/PUPRemote")
```

## LVGL 9.0
This is still experimental. The examples on [LVGL 9.0](https://docs.lvgl.io/master) are not yet in sync with the [LVGL 9.0 emulator](https://sim.lvgl.io/v9.0/micropython/ports/javascript/index.html).

Differences:
- buttons -> btn
- image -> img
- ... and possible other incosistancies

