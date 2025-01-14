#!/bin/fish


./bin/esptool.py --port "$ESP32_PORT" erase_flash
./bin/esptool.py --port "$ESP32_PORT" --baud 1000000 write_flash --flash_size=4MB -fm dio 0 ESP8266_GENERIC-20241129-v1.24.1.bin
