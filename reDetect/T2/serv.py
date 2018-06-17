from testdir.module import a
from testdir.module import b

def reimported():
	print("Re-import succeed")
	
def imp():
	print(b[0])
	if b[0] == 0:
		print(222)
		a(b).add('a',1)
		
imp()


