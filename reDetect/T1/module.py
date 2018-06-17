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
		#print("Func of inspect:",dir(inspect))
		frame = inspect.currentframe()
		e = frame.f_back
		mod = inspect.getmodule(e)
		print(dir(mod))
		
		c = inspect.getouterframes(frame)
		print(c)
		self.dict[k] = v
		