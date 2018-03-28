from unqlite import UnQLite

udb = UnQLite('utest.db')

#Basic
udb['a'] = '1' #like a dict
content = [ '%s=%s' % item for item in udb ] #db iterable
print(content)

#Cursor
C = udb.cursor()
content2 = [ '%s=%s' % (k,v) for k,v in C] #iter differently
C.seek('a')
print(C.value()) #seems not only an iteritor, it can go backward

#VM


#Collecton -- Storage dicts in list (I think...)
usr = udb.collection('usr')
usr.create() #this is necesary
u1 = {'name':'neet','uuid':'D7B810FD'}  #serialize and save
'''
('usr', b'a\x1e\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x02L\\\x0b\xb5')
('usr_0', '\x01\x08\x00\x00\x00\x04name\x05\x08\x00\x00\x00\x04neet\x06\x08\x00\x00\x00\x04uuid\x05\x08\x00\x00\x00\x08D7B810FD\x06\x08\x00\x00\x00\x04__id\x05\n\x00\x00\x00\x00\x00\x00\x00\x00\x06\x02')
('usr_1', '\x01\x08\x00\x00\x00\x04name\x05\x08\x00\x00\x00\x05limbo\x06\x08\x00\x00\x00\x04uuid\x05\x08\x00\x00\x00\x08D7B810FC\x06\x08\x00\x00\x00\x04__id\x05\n\x00\x00\x00\x00\x00\x00\x00\x01\x06\x02')
Well, 'collection' is also serialized
'''
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

udb.close()




