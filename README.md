# wiggle

## dependencies
#### *gpiozero + numpy*
```
sudo apt-get update
sudo apt-get install python3-gpiozero python3-numpy
```

## connections
#### *Adafruit TB6612 breakout board*
[link to the breakout](https://learn.adafruit.com/adafruit-tb6612-h-bridge-dc-stepper-motor-driver-breakout/overview)
```
raspi connections to breakout board:
    3.3V -> VCC
    GND -> GND
    GPIO17 -> PMWA
    GPIO5  -> AIN1
    GPIO6  -> AIN2
    GPIO18 -> PMWB
    GPIO13 -> BIN1
    GPIO19 -> BIN2

Motor terminals connected to MOTORA outputs on breakout board
12V power supply connected to VMOTOR power inputs on breakout board:
```

using [this vibration motor](https://www.amazon.com/gp/product/B00AKWRZPQ/ref=oh_aui_detailpage_o05_s00?ie=UTF8&psc=1)
