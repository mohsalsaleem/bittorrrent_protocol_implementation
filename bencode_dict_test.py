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

value = bencode.debencodedict("d4:spami2e6:saleemi3ee")
if type(value) is dict and set(value) == set({'saleem': 3, 'spam': 2}):
	assertion_count += 1
else:
	error_count += 1


if error_count > 0:
	print "Status: Fail"
else:
	print "Status: Success"

print "Asserts: "+str(assertion_count)+", Errors:"+str(error_count) 	