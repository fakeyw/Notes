import inspect
import os
import re
pa = re.compile(r".*[\\|\/](.*)\.py")

b = [0]

class a(object):
	def __init__(self,b):
		self.dict = {}
		self.b = b
		
	def add(self,k,v):
		b[0] = 1
		a = inspect.currentframe().f_back
		who = inspect.getframeinfo(a)
		fname = who.filename
		print(fname,type(fname))
		target = __import__(fname[:-3])
		#print(dir(target))
		self.dict[k] = v
		