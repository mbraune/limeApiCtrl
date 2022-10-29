"""
limeProc.py

---
interactive control LimeTxcw.exe
    via subprocess, uses stdin + stdout
    text only
-
- open points : nonblocking readline() , timeout, error output
"""
import subprocess
from subprocess import Popen, PIPE
import time

class LimeProc:
    def __init__(self, cmdPath, timeout=10):
        """ open pipe with path to cmd """
        self.p = Popen(cmdPath, text=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)

        if self.alive():
            self.__read(0.5)  # flush initial startup messages 
            if self.query('devid')[0] == True:
                self.instId = self.query('devid')[1]
                print("LimeSDR-Mini serial ", self.instId)
            else:
                print("error initializing Lime")
        else:
            print("error creating Lime process ",cmdPath)

    def __read(self, twait=0):
        """ private
            readline until cmd_ok or err_ in response
            return True/False, res0, res1, ..
            run this only after init or write, else readline hangs
        """
        line = ""
        resp = []
        while not ('cmd_ok' in line or 'err_' in line) :
            line = self.p.stdout.readline()
            resp.append(line.strip())
        if ('cmd_ok' in resp[-1]):
            time.sleep(twait)
            if len(resp) == 1:
                return True
            elif len(resp) == 2:
                return True, resp[0]
            elif len(resp) == 3:
                return True, resp[0], resp[1]
            else:
                return True, resp
        else:
            return False, resp
        #return ('cmd_ok' in resp), resp.replace("cmd_ok","").strip()

    def __write(self, cmd, twait=0):
        """ private 
            write command to process, 
            return True if process alive
        """
        if self.alive():
            msg = f'{cmd}\n'
            self.p.stdin.write(msg)
            self.p.stdin.flush()
            time.sleep(twait)
            return True
        else:
            return False
##
# end private functions
##

    def alive(self):
        """ return True if process is alive """
        return (self.p.poll() == None)

    def close(self):
        """ close connection """
        self.__write('close')
        self.p.kill()
        return True;

    def query(self, cmd, twait=0):
        """ send write and read,  
            if ok return tuple (True, res0,..)
            else  return False
        """
        #print("query twait ", twait)
        if self.__write(cmd,twait):
            return self.__read(twait)
        else:
            return False;

##-------------------------------------------------------------
