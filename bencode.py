def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        #print "Error"
        return False

def debencodelist(ben):#Decode bencoded List
    decoded_list = [] #an empty list
    if ben[0] == "l" and ben[len(ben)-1] == "e" and len(ben) == 2:
        return decoded_list
        #print decoded_list
    elif ben[0] != "l" or ben[len(ben)-1] != "e":
        return "Oops, Looks like you didnt send a bencoded list!"
        #print "Oops, Looks like you didnt send a bencoded list!"
    elif ben[0] == "l" and ben[len(ben)-1] == "e" and len(ben) > 2:
        # print "String to be decoded is: "+ben
        i = 1
        # print "Hello"
        while i < len(ben):
            #if i != 0 or i != len(ben)-1:
                el = ""
                if RepresentsInt(ben[i]):
                    ef = ben[i]
                    while (RepresentsInt(ben[i])):
                        el += ben[i]
                        i += 1
                    i -= 1
                if RepresentsInt(ben[i]) and ben[i+1] == ":":
                    listElement = ""
                    elementLength = int(el)
                    i+=2
                    if i+elementLength == len(ben):
                        return "Something Wrong!"
                    else:
                        # print "Element Length: "+str(elementLength),
                        # print ",Element is: ",
                        for x in range(i,i+elementLength):
                            # print ben[x],
                            listElement += ben[x]
                        decoded_list.append(listElement)    
                        # print "\n"    
                        i += elementLength    
                        # print "Saleem"
                        # print i
                        # print elementLength    
                        # print len(ben)
                        if i == len(ben)-1:
                            break
        return decoded_list                    

def debencodedict(ben):
    decoded_dict = {} #an empty dict
    if ben[0] == "d" and ben[len(ben)-1] == "e" and len(ben) == 2:
        return decoded_dict
        #print decoded_dict
    elif ben[0] != "d" or ben[len(ben)-1] != "e":
        return "Oops, Looks like you didnt send a bencoded dict!"
        #print "Oops, Looks like you didnt send a bencoded dict!"
    elif ben[0] == "d" and ben[len(ben)-1] == "e" and len(ben) > 2:
        key = True
        past_key = ""
        #for i in range(len(ben)):
        i = 1
        while i < len(ben):
            #print ben[i]+" : "+str(i)
            if i != 0 and i != len(ben)-1:
                el = ""
                if RepresentsInt(ben[i]):
                    ef = ben[i]
                    while (RepresentsInt(ben[i])):
                        el += ben[i]
                        i += 1
                    i -= 1        
                if RepresentsInt(ben[i]) and ben[i+1] == ":":
                    dict_value = ""
                    elementLength = int(el)#int(ben[i])
                    i+=2
                    if i+elementLength == len(ben):
                        return "Something Wrong!"
                    else:
                        for x in range(i,i+elementLength):
                            dict_value += ben[x]
                        if past_key != "":
                            decoded_dict[past_key] = dict_value
                      #      print decoded_dict
                            past_key = ""
                            key = True
                            i += elementLength
                            continue        
                        if key:
                            past_key = dict_value
                            key = False
                        i += elementLength

            else:
                i += 1                                 
        return decoded_dict
                         
    else:
        return "Something Wrong!"   
            
        
def debencodeint(ben):
    decoded_integer = ""
    i = 1
    if ben[0] != "i" or ben[len(ben)-1] != "e":   
        return "Oops, Looks like you didnt send a bencoded int!"
    elif ben[0] == "i" and ben[1] == "e" and len(ben) == 2:
        return 0
    elif not RepresentsInt(ben[1]):
        return "There is no integer"
    elif RepresentsInt(ben[i]) or ben[i] == "+" or ben[i] == "-":
        while( RepresentsInt(ben[i]) ):
            decoded_integer += ben[i]
            i += 1
        if RepresentsInt(decoded_integer) and len(decoded_integer) == ( len(ben) - 2 ):
            return int(decoded_integer)
    else:
        return "Something Wrong!"
