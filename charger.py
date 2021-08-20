#!/usr/bin/env python

# Copyright 2021 Venky Raju
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import RPi.GPIO as GPIO

CHARGER_SSR_CTL = 17

def _init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(CHARGER_SSR_CTL, GPIO.OUT) # GPIO Assign mode

def charger_off():
    _init()
    GPIO.output(CHARGER_SSR_CTL, GPIO.LOW) # off

def charger_on():
    _init()
    GPIO.output(CHARGER_SSR_CTL, GPIO.HIGH) # on

def is_charger_on():
    _init()
    return GPIO.input(CHARGER_SSR_CTL) == GPIO.HIGH

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Charger is {}".format("ON" if is_charger_on() else "OFF"))
    elif (sys.argv[1] == "on"):
        charger_on()
        print("Charger is ON")        
    else:
        charger_off()
        print("Charger is OFF")