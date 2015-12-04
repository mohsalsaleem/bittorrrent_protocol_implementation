import bencode

assertion_count = 0
error_count = 0

value = bencode.debencodedict("de")
print value
if type(value) is dict and set(value) == set({}):
	assertion_count += 1
else:
	error_count += 1	

value = bencode.debencodedict("d9:publisher3:bob17:publisher-webpage15:www.example.com18:publisher.location4:homee")
print value
if type(value) is dict and set(value) == set({'publisher': 'bob', 'publisher-webpage': 'www.example.com', 'publisher.location': 'home'}):	
	assertion_count += 1
else:
	error_count += 1

value = bencode.debencodedict("d4:spam6:saleem")
print value
if type(value) is str and value == "Oops, Looks like you didnt send a bencoded dict!":
	assertion_count += 1
else:
	error_count += 1

value = bencode.debencodedict("d4:spam6:saleee")
print value
if type(value) is str and value == "Something Wrong!":
	assertion_count += 1
else:
	error_count += 1


if error_count > 0:
	print "Status: Fail"
else:
	print "Status: Success"

print "Asserts: "+str(assertion_count)+", Errors:"+str(error_count) 	