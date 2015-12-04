import bencode

assertion_count = 0
error_count = 0

value = bencode.debencodeint("ie")
if type(value) is int and value == 0:
	assertion_count += 1
else:
	error_count += 1

value = bencode.debencodeint("i22333424e")
if type(value) is int and value == 22333424:
	assertion_count += 1
else:
	error_count += 1

value = bencode.debencodeint("2223e")
if type(value) is str and value == "Oops, Looks like you didnt send a bencoded int!":
	assertion_count += 1
else:
	error_count += 1

value = bencode.debencodeint("iee")
if type(value) is str and value == "There is no integer":
	assertion_count += 1
else:	
	error_count += 1


if error_count > 0:
	print "Status: Fail"
else:
	print "Status: Success"

print "Asserts: "+str(assertion_count)+", Errors:"+str(error_count) 	