# limeApiCtrl
interactive control LimeApiTx

## limeProc items
control limeApiTx.exe via python 
uses subprocess , popen

## python subprocess
````
import subprocess
from subprocess import Popen, PIPE
cmd = ['d:\\tools\\limeApiTx\\LimeTxCw.exe']
p = Popen(cmd, text=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)

print(p.poll())			None

p.stdout.readline()
..
.
p.stdout.readline()							'\tfreq    = 1575.419998 MHz  \t   gain = 20 dB\n'
p.stdout.readline()							'cmd_ok\n'

p.stdin.write('getchiptemperature(0)\n')	22
p.stdin.flush()

>>> p.stdout.readline()				'\t32.7333\n'
>>> p.stdout.readline()				'cmd_ok\n'
````

## class LimeProc 

### interface :
- **LimeProc(cmdPath)** constructor
- **alive()**       return True/False
- **close()**       return True
- **query(cmd,twait)**    return Tuple (True/False, res0, res1, ...)
- **instId**        return deviceID

### example:
    """Tests init lime """
    limecmd = ['d:\\tools\\limeApiTx\\LimeTxCw.exe']
    lime = LimeProc(limecmd)

    print(lime.instId)
    print(lime.query('getchiptemperature(0)'))
    print(lime.query('getsamplerate(tx,0)'))
    lime.close()

output
````
(base) ..\limeApiCtrl>python lime_test1.py
LimeSDR-Mini serial  1D4C38442B51E1
1D4C38442B51E1
(True, '43.2476')
(True, '15.36 MHz', '15.36 MHz')
````
### open: timeout in constructor ?
### open: nonblocking readline



