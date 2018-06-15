## werkzeug的全局变量路由

在flask中可以用类似全局变量的方式`request.form`等对当前http连接的参数进行调用。但这种全局变量产生的方式并不是直接声明，否则在平发和协程时会冲突。

```python
_request_ctx_stack = LocalStack()
current_app = LocalProxy(lambda: _request_ctx_stack.top.app)
request = LocalProxy(lambda: _request_ctx_stack.top.request)
session = LocalProxy(lambda: _request_ctx_stack.top.session)
g = LocalProxy(lambda: _request_ctx_stack.top.g)
```

与`threading.local`不同的是`werkzeug.local`支持协程的全局变量分离

