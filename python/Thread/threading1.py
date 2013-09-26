import string, threading, time

def thread_main(a):
	global count, mutex
	threadname = threading.currentThread().getName()

	for x in xrange(0, int(a)):
		#取锁
		mutex.acquire()
		count = count+1
		#释放锁
		mutex.release()
		print threadname, x, count
		time.sleep(1)

def main(num):
	global count, mutex
	thread = []

	count = 1
	#创建锁
	mutex = threading.lock()
	for x in xrange(0, num):
		threads.append(threading.Thread(target=thread_main, args=(10,)))
	#启动所有线程
	for t in threads:
		t.start()
	#主线程等待所有子线程推出
	for t in threads:
		t.join()
	
if __name__ == '__main__':
	num = 4
	main(num)
