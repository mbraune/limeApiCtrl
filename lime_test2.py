"""
lime_test2.py : loop over freq

---
drive LimeTxApi 
use class LimeProc
generic setfreq function: 
     after switch on sometimes amplitude ~30dB to low, 
     resending setsamplerate fixes it 
"""
from limeproc import LimeProc
import time
##-------------------------------------------------------------

def init(lprc):
    """ init lime for tx"""
    print("Init             ", lprc.query('init()'))
    setout(lprc, False)
    print("Tx Antenna Auto  ", lprc.query('setantenna(tx,0,2)'))

def status(lprc):
    """ print settings"""
    print("ChipTemperature  ", lprc.query('getchiptemperature(0)'))
    print("Tx Antenna       ", lprc.query('getantenna(tx,0)'))
    print("Tx Samplerate    ", lprc.query('getsamplerate(tx,0)'))
    print("Clockfreq 0      ", lprc.query('getclockfreq(0)'))
    print("Clockfreq 1      ", lprc.query('getclockfreq(1)'))
    print("Clockfreq 2      ", lprc.query('getclockfreq(2)'))
    print("GainDB           ", lprc.query('getgaindb(tx,0)'))
    time.sleep(0.4)

def setfreq(lprc, frq):
    """set output off before changing freq """
    setout(lprc, False)
    cmd = f'setlofrequency(tx,0,{frq})'
    lprc.query(cmd, 0.4)  # 1.0
    setout(lprc, True)
    cmd = f'setsamplerate(10,1)'
    return(lprc.query(cmd, 0.2))

def setgain(lprc, gain):
    cmd = f'setgaindb(tx,0,{gain})'
    return(lprc.query(cmd, 0.2))

def setout(lprc, on):
    if on == True:
        cmd = f'enablechannel(tx,0,1)'
    else: 
        cmd = f'enablechannel(tx,0,0)'
    return lprc.query(cmd)

# ---------------------------------------------------------------
# ---------------------------------------------------------------
def main():
    limecmd = ['d:\\tools\\limeApiTx\\LimeApiTx.exe']
    lime = LimeProc(limecmd)

    init(lime)
    status(lime)

    setgain(lime,40)
    for f in range(1690, 1711, 10):
        print("f ",f)
        setfreq(lime, f)
        time.sleep(2)

    setout(lime, False)
    status(lime)
    lime.close()


if __name__ == '__main__':
    main()