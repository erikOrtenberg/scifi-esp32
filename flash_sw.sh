#!/bin/fish

ampy --port "$ESP32_PORT" put src
ampy --port "$ESP32_PORT" put boot.py
ampy --port "$ESP32_PORT" put main.py
