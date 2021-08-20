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

import serial
from bms.jbd import JBD

PORT='/dev/ttyUSB0'

def get_status():
    port=serial.Serial(PORT)
    bms=JBD(port)

    status = read_bms(bms)
    if (status == None):
        print("Trying again...")
        status = read_bms(bms)

    if (status == None):
        return None, None, None
    
    voltage=status.get('pack_mv')/1000
    current=status.get('pack_ma')/1000
    soc=status.get('cap_pct')
    cur_cap=status.get('cur_cap')
    full_cap=status.get('full_cap')
    return voltage, current, soc, cur_cap, full_cap
    
def read_bms(bms):
    try:
        return bms.readBasicInfo()
    except Exception:
        return None

if __name__ == "__main__":
    voltage, current, soc, cur_cap, full_cap = get_status()
    print("{:.1f}V {:.1f}A {}% {}mAH {}mAH".format(voltage, current, soc, cur_cap, full_cap))
