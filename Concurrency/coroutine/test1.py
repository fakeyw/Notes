import asyncio
import time
@asyncio.coroutine
def slp(len):
	time.sleep(len)
	yield

@asyncio.coroutine
def hello():
	print("Hello world!")
	# 异步调用asyncio.sleep(1):
	#r = yield from slp(5)
	r = yield from asyncio.sleep(5)
	print("Hello again!")

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

#这个实验说明不了太多东西，只是对比sleep与asyncio.sleep()
#结果有点奇怪

#sleep
#------------
#Hello world!
#(...5s...)
#Hello world!
#(...5s...)
#Hello again!
#Hello again!

#asyncio.sleep
#------------
#Hello world!
#Hello world!
#(...5s...)
#Hello again!
#Hello again!

