import threading
import time

__LOCK__=threading.Lock()

pub_src_1 = []
pub_src_2 = []

def f_to_take_1():
	__LOCK__.acquire()
	pub_src_1.append(1)
	time.sleep(5)
	print(pub_src_2) #if even [], t2 can't take src because of the LOCK
	time.sleep(10)
	__LOCK__.release()
	return
	
def f_to_take_2():
	time.sleep(3)
	__LOCK__.acquire()
	pub_src_2.append(2)
	__LOCK__.release()
	return 
	
t1 = threading.Thread(target=f_to_take_1)
t2 = threading.Thread(target=f_to_take_2)
t1.start()
t2.start()
t1.join()
t2.join()

'''
$ python basic_test.py
[]
'''
