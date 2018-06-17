from module import a
from module import b
from module import c

def reimported():
	print("Re-import succeed")
	
def imp():
	c()
	print(b[0])
	if b[0] == 0:
		print(222)
		a(b).add('a',1)


