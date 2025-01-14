# ESP32 project

## Dependencies
* `picocom` - For entering REPL
* `ampy` - For copying files to the chip
* `python and pip` - lol ofc.

## Python dependencies
All of the following should be in a python `venv` located at the root directory of the project. 

* `esptool` 

## Guides and links

* The used chips manufacturer website [page](https://www.wemos.cc/en/latest/d1/d1_mini.html)

* Getting started guide for micropython on this chip. [Link](https://www.wemos.cc/en/latest/tutorials/d1/get_started_with_micropython_d1.html)

* Firmware [download](https://micropython.org/download/ESP8266_GENERIC/)

## How to use

* `env.sh` sets the `ESP32_PORT` variable. This variable is used in subsequent scripts.

* `flash_firmware.sh` flashes the firmware to the chip. Expects the firmware binary to be located in the same folder

* `flash_sw.sh` flashes the entire `src` directory to the chip. Also updates `boot.py` to run a specified top module (NOT IMPLEMENTED YET).

* `repl.sh` attaches to the UART serial connection available from the chip.  
