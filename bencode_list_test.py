import bencode

assertion_count = 0
error_count = 0

value = bencode.debencodelist("le")
if type(value) is list and set(value) == set([]):
	assertion_count += 1
else:
	error_count += 1	

value = bencode.debencodelist("l4:spam6:saleeme")
if type(value) is list and set(value) == set(['spam','saleem']):	
	assertion_count += 1
else:
	error_count += 1

value = bencode.debencodelist("l4:spam6:saleem")
if type(value) is str and value == "Oops, Looks like you didnt send a bencoded list!":
	assertion_count += 1
else:
	error_count += 1

value = bencode.debencodelist("l4:spam6:saleee")
if type(value) is str and value == "Something Wrong!":
	assertion_count += 1
else:
	error_count += 1


if error_count > 0:
	print "Status: Fail"
else:
	print "Status: Success"

print "Asserts: "+str(assertion_count)+", Errors:"+str(error_count) 	