import threading
import time
import keyword
#print(keyword.kwlist)
#print(keyword)

num = 5

cd = threading.Condition()

class t1(threading.Thread):
	def __init__(self,*args,**kw):
		super(t1,self).__init__(*args,**kw)
		
	def run(self):
		global num
		print('[-1]','start')
		while True:
			with cd:
				if num > 3:
					num -= 1
					print('[-1]',num)
					cd.notify()
				else:
					cd.wait()
			
class t2(threading.Thread):
	def __init__(self,*args,**kw):
		super(t2,self).__init__(*args,**kw)
		
	def run(self):
		global num
		print('[+1]','start')
		while True:
			with cd:
				if num < 7:
					num += 1
					print('[+1]',num)
					cd.notify()
				else:
					cd.wait()
tt1 = t1()
tt2 = t2()
tt1.start()
tt2.start()

#结论是condition的功能是条件操作


