想找个类似sqlite这种作为文件保存的但为Nosql的数据库

然后找到了Unqlite

[官方文档](http://unqlite-python.readthedocs.io/en/latest/installation.html)

---

先安装一下

```pip install unqlite```

这一数据库的python连接库是需要Cython扩展的

```pip install Cython```

又有 `Microsoft Visual C++ 14.0 is required`

下载安装 [c++ 14 运行库](https://go.microsoft.com/fwlink/?LinkId=746572)

好像还不够 必须要build tools

 [Visual C++ 2015 Build Tools](http://go.microsoft.com/fwlink/?LinkId=691126&fixForIE=.exe.) 不带Visual Studio的

> 来自 https://stackoverflow.com/questions/44951456/pip-error-microsoft-visual-c-14-0-is-required

然后再执行pip安装就好了

---

**基本使用**

```python
from unqlite import UnQLite
udb = UnQLite('utest.db')
udb['a'] = '1' #like a dict
content = [ '%s=%s' % item for item in udb ] #db iterable
```

**Cursor**

```python
C = udb.cursor()
content2 = [ '%s=%s' % (k,v) for k,v in C] #iter differently
C.seek('a')
print(C.value()) #seems not only an iteritor, it can go backward
```

**Collection**

```python
usr = udb.collection('usr')
usr.create() #this is necesary
u1 = {'name':'neet','uuid':'D7B810FD'}  #serialize and save
'''
('usr', b'a\x1e\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x02L\\\x0b\xb5')
('usr_0', '\x01\x08\x00\x00\x00\x04name\x05\x08\x00\x00\x00\x04neet\x06\x08\x00\x00\x00\x04uuid\x05\x08\x00\x00\x00\x08D7B810FD\x06\x08\x00\x00\x00\x04__id\x05\n\x00\x00\x00\x00\x00\x00\x00\x00\x06\x02')
('usr_1', '\x01\x08\x00\x00\x00\x04name\x05\x08\x00\x00\x00\x05limbo\x06\x08\x00\x00\x00\x04uuid\x05\x08\x00\x00\x00\x08D7B810FC\x06\x08\x00\x00\x00\x04__id\x05\n\x00\x00\x00\x00\x00\x00\x00\x01\x06\x02')
Well, 'collection' is also serialized
'''
```

然而这不是一般使用的pickle序列化，所以不太好解。

```python
usr.store(u1)
n = usr.filter(lambda o:o['name'] == 'neet')
#filter? seems doesn't have searching function
#but i can give it that~
print(n)

def muti_store(db,coll,uuid,dic):
	next = coll.last_record_id() + 1
	db[uuid] = next
	coll.store(dic)
	return True

def search(db,coll,uuid):
	return coll.fetch(int(db[uuid]))
	
u2 = {'name':'limbo','uuid':'D7B810FC'} 
muti_store(udb,usr,'D7B810FC',u2)
n2 = search(udb,usr,'D7B810FC')
print(n2)
```

collection是不存在查找功能的，得自己建立索引

想再次获取这个collection：

```python
usr = udb.collection('usr')
```

**Save**

```python
udb.close()
```

记得保存