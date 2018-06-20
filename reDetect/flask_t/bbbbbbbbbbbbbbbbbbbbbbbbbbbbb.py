import cccccccccccccccccccc
import sys
for k,v in sys.modules.items():
	#print(dir(v))
	try:
		print(v.__file__)
	except Exception as e:
		pass
def c():
	v=6