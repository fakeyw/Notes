import threading
import time

e1 = threading.Event()
e2 = threading.Event()
e1.set()
e2.set()

class t1(threading.Thread):
	def __init__(self,*args,**kw):
		super(t1,self).__init__(*args,**kw)
		
	def run(self):
		global e1
		print('e1 chocked')
		e1.clear()
		time.sleep(5)
		print('e1 notify')
		e1.set()
		
		
class t2(threading.Thread):
	def __init__(self,*args,**kw):
		super(t2,self).__init__(*args,**kw)
		
	def run(self):
		global e2
		time.sleep(2)
		print('wait for e2')
		e2.wait()
		print('ok')

tt1 = t1()
tt2 = t2()
tt1.start()
tt2.start()

#结论是两个event相互独立，等待队列也是独立的

		