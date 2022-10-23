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

class LimeProc:
    def __init__(self, cmdPath, timeout=10):
        """ open pipe with path to cmd """
        self.p = Popen(cmdPath, text=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)

        if self.alive():
            self.__read()  # flush initial startup messages 
            if self.query('devid')[0] == True:
                self.instId = self.query('devid')[1]
                print("LimeSDR-Mini serial ", self.instId)
            else:
                print("error initializing Lime")
        else:
            print("error creating Lime process ",cmdPath)

    def __read(self):
        """ private
            readline until cmd_ok or err_ in response
            return True/False, res0, res1, ..
            run this only after init or write, else readline hangs
        """
        resp = ""
        while not ('cmd_ok' in resp or 'err_' in resp) :
            resp += self.p.stdout.readline()
        return ('cmd_ok' in resp), resp.replace("cmd_ok","").strip()

    def __write(self, cmd):
        """ private 
            write command to process, 
            return True if process alive
        """
        if self.alive():
            msg = f'{cmd}\n'
            self.p.stdin.write(msg)
            self.p.stdin.flush()
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

    def query(self, cmd):
        """ send write and read,  
            if ok return tuple (True, res0,..)
            else  return False
        """
        if self.__write(cmd):
            return self.__read()
        else:
            return False;

##-------------------------------------------------------------
