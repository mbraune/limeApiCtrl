"""
lime_test1.py

---
drive LimeTxApi 
use class LimeProc
"""
from limeproc import LimeProc
import time
##-------------------------------------------------------------

def lime_example1():
    """Tests init lime """
    limecmd = ['d:\\tools\\limeApiTx\\LimeTxCw.exe']
    lime = LimeProc(limecmd)

    print(lime.instId)
    print(lime.query('getchiptemperature(0)'))
    print(lime.query('getsamplerate(tx,0)'))
    lime.close()


def lime_example2():
    """ init lime , set freq"""
    limecmd = ['d:\\tools\\limeApiTx\\LimeTxCw.exe']
    lime = LimeProc(limecmd)

    print("devid", lime.instId)
    print("ChipTemperature  ", lime.query('getchiptemperature(0)'))
    print("Tx Antenna       ", lime.query('getantenna(tx,0)'))
    print("Tx Samplerate    ", lime.query('getsamplerate(tx,0)'))
    print("LO Freq          ", lime.query('getlofrequency(tx,0)'))

    print("Clockfreq 0      ", lime.query('getclockfreq(0)'))
    print("Clockfreq 1      ", lime.query('getclockfreq(1)'))
    print("Clockfreq 2      ", lime.query('getclockfreq(2)'))
    print("NormalizedGain   ", lime.query('getnormalizedgain(tx,0)'))


    print("LO Freq 1600     ", lime.query('setlofrequency(tx,0,1600)'))
    print("NormalizedGain   ", lime.query('setnormalizedgain(tx,0,0.3)'))
    print("EnableChannel On ", lime.query('enablechannel(tx,0,1)'))
    print("Samplerate 12,4  ", lime.query('setsamplerate(12,4)'))
    lime.close()


def main():
    lime_example1()

if __name__ == '__main__':
    main()