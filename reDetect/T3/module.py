import inspect
import os
import re
pa = re.compile(r".*[\\|\/](.*)\.py")

b = [0]

def c():
	a = inspect.currentframe().f_back
	who = inspect.getframeinfo(a)
	print(who)


class a(object):
	def __init__(self,b):
		self.dict = {}
		self.b = b	
		
	def add(self,k,v):
		b[0] = 1
		a = inspect.currentframe().f_back
		#print(a)
		who = inspect.getframeinfo(a)
		print(who)
		#print(dir(who))
	
		fname = who.filename
	
		#print(fname)
		#res = pa.match(fname)
		#print(res)
	
		#rpath = os.path.dirname(os.path.realpath(__file__))
		#print(rpath)
		print(fname,type(fname))
		target = __import__(fname[:-3])
		#print(dir(target))
		self.dict[k] = v
		