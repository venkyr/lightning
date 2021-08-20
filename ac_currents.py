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

import math
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from enum import Enum

LINE_IN = 1
CHARGER_IN = 2
INVERTER_OUT = 0

sensor_factors = [10,10,15]
i2c = busio.I2C(board.SCL, board.SDA)
ads_1 = ADS.ADS1015(i2c,gain=2,data_rate=3300,address=0x48)
ads_2 = ADS.ADS1015(i2c,gain=2,data_rate=3300,address=0x49)

chan = [
    AnalogIn(ads_1, ADS.P0, ADS.P1),
    AnalogIn(ads_1, ADS.P2, ADS.P3),
    AnalogIn(ads_2, ADS.P0, ADS.P1)
]

def get_ac_currents():

    sq_sum = 0
    num_samples = 300
    currents = [0,0,0]
    for sensor in range(3):
        for sample in range(num_samples):
            voltage = chan[sensor].voltage
            sq_sum += voltage*voltage
        currents[sensor] = round(math.sqrt(sq_sum/num_samples) * sensor_factors[sensor],2)
        sq_sum = 0

    
    return currents[CHARGER_IN], currents[LINE_IN], currents[INVERTER_OUT]

if __name__ == "__main__":
    charger_in, line_in, inverter_out = get_ac_currents()
    print("Charger in: {}A".format(charger_in))
    print("Line in: {}A".format(line_in))
    print("Inverter out: {}A".format(inverter_out))



