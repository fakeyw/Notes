import asyncio
import threading

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    print("Main",threading.currentThread())
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['localhost','localhost','localhost']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

#在服务器中，接收到的第一个请求会被sleep(10)，第二个请求立即返回
#运行结果中，第二个请求正常返回了，在此期间第一个请求处于阻塞中
#这一实验证明 协程的IO是并发的，不会阻塞