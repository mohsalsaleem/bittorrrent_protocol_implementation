import bencode

print "\n--------------Dictionary------------"

assertion_count = 0
error_count = 0

value = bencode.debencodedict("de")
if type(value) is dict and set(value) == set({}):
	assertion_count += 1
else:
	error_count += 1	

value = bencode.debencodedict("d9:publisher3:bob17:publisher-webpage15:www.example.com18:publisher.location4:homee")
if type(value) is dict and set(value) == set({'publisher': 'bob', 'publisher-webpage': 'www.example.com', 'publisher.location': 'home'}):	
	assertion_count += 1
else:
	error_count += 1

value = bencode.debencodedict("d4:spam6:saleem")
if type(value) is str and value == "Oops, Looks like you didnt send a bencoded dict!":
	assertion_count += 1
else:
	error_count += 1

value = bencode.debencodedict("d4:spam6:saleee")
if type(value) is str and value == "Something Wrong!":
	assertion_count += 1
else:
	error_count += 1

value = bencode.debencodedict("d8:announce35:udp://tracker.openbittorrent.com:8013:creation datei1327049827e6:lengthi20e4:name10:sample.txt12:piece lengthi65536e6:pieces20:asdfghjklpoiuytrewqae")
if type(value) is dict and set(value) == set({'piece length': 65536, 'name': 'sample.txt', 'creation date': 1327049827, 'pieces': 'asdfghjklpoiuytrewqa', 'length': 20, 'announce': 'udp://tracker.openbittorrent.com:80'}):
	assertion_count += 1
else:
	error_count += 1


if error_count > 0:
	print "Status: Fail"
else:
	print "Status: Success"

print "Asserts: "+str(assertion_count)+", Errors:"+str(error_count) 	