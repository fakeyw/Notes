from flask import Flask
import time
import threading
import imp_t
import asyncio

app = Flask(__name__)
count = [0]

@app.route('/')
def hello_world():
	if count[0] == 0:
		count[0] = 1
		print("sleep")
		time.sleep(3)
		#imp_t.a()
	return 'Hello Flask!'

if __name__ == '__main__':
    app.run("127.0.0.1",port=80,threaded=True,debug=True)