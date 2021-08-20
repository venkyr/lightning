#!/usr/bin/env python

import serial
import jbd

PORT='/dev/ttyUSB0'

def get_status():
    port=serial.Serial(PORT)
    bms=jbd.JBD(port)

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
