# -*- coding:utf-8 -*-
import threading
import Queue
import time

class InThread(threading.Thread):
    def run(self):
        time.sleep(1)
        if mutexi.acquire(1):
            msg = raw_input("输入消息:");
            q.put(msg,False)
            mutexi.release()

class OutThread(threading.Thread):
    def run(self):
        time.sleep(1)
        if mutexo.acquire(1):
            print "输出消息: %s" % q.get(False)
            mutexo.release()

mutexi = threading.Lock()
mutexo = threading.Lock()
q = Queue.Queue(10)
def test():
    for i in range(10):
        t1 = InThread()
        t1.start()
        t2 = OutThread()
        t2.start()

if __name__ == '__main__':
    test()

        
