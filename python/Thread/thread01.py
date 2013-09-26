# -*- coding:utf-8 -*-

import threading 
import time

class Mythread(threading.Thread):
    def run(self):
        global num
        while True:
            time.sleep(1)
            if mutex.acquire(1):
                num = num+1
                msg = self.name+' set num '+str(num)+'\n'
                print msg
                mutex.release()

num = 0
mutex = threading.Lock()
def test():
    for i in range(5):
        thread01 = Mythread()
        thread01.start()
    

if __name__ == '__main__':
    test()


