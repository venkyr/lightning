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

INVERTER_RELAY_CTL = 18

def _init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(INVERTER_RELAY_CTL, GPIO.OUT) # GPIO Assign mode

def inverter_off():
    _init()
    GPIO.output(INVERTER_RELAY_CTL, GPIO.HIGH) # off; active low

def inverter_on():
    _init()
    GPIO.output(INVERTER_RELAY_CTL, GPIO.LOW) # on; active low

def is_inverter_on():
    _init()
    return GPIO.input(INVERTER_RELAY_CTL) == GPIO.LOW

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Inverter is {}".format("ON" if is_inverter_on() else "OFF"))
    elif (sys.argv[1] == "on"):
        inverter_on()
        print("Inverter is ON")
    else:
        inverter_off()
        print("Inverter is OFF")
        