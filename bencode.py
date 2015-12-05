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
                    if ben[i+1] == ":":
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
                elif ben[i] == "i" and ( ben[i+1] == "+" or ben[i+1] == "-" or RepresentsInt(ben[i+1])) and ben[i+2] != ":":
                    bencoded_int = "i"
                    x = 0
                    if ben[i+1] == "+":
                        x = i + 2
                        bencoded_int += "+" 
                    elif ben[i+1] == "-":
                        x = i + 2
                        bencoded_int += "-"
                    else:
                        x = i + 1    
                        # print "X is: " + str(x)
                        # print ben[x]
                    while(RepresentsInt( ben[x] )):
                        # print "ben[x] in is:" + str(ben[x])
                        # print "x in is" + str(x)
                        x += 1    
                    # print ben[i]
                    to_decode = ben[i:x+1]
                    # print to_decode + " value"
                    decoded_int = debencodeint(to_decode)
                    # print decoded_int
                    decoded_list.append(int(decoded_int))
                    # print decoded_list
                    i = x + 1
                    # print ben[i] + str(i)
                    continue
                elif i == len(ben) - 1:    
                    return decoded_list            
        return decoded_list                    

def debencodedict(ben):
    decoded_dict = {} #an empty dict
    past_key = ""
    if ben[0] == "d" and ben[len(ben)-1] == "e" and len(ben) == 2:
        return decoded_dict
        #print decoded_dict
    elif ben[0] != "d" or ben[len(ben)-1] != "e":
        return "Oops, Looks like you didnt send a bencoded dict!"
        #print "Oops, Looks like you didnt send a bencoded dict!"
    elif ben[0] == "d" and ben[len(ben)-1] == "e" and len(ben) > 2 and past_key == "":
        key = True
        #for i in range(len(ben)):
        i = 1
        while i < len(ben):
            #print ben[i]+" : "+str(i)
            # print ben[i] + " Starting " + str(i)
            if i != 0 and i != len(ben)-1:
                el = ""
                if RepresentsInt(ben[i]):
                    # print "Reaching"
                    ef = ben[i]
                    while (RepresentsInt(ben[i])):
                        el += ben[i]
                        i += 1
                    i -= 1        
                    if ben[i+1] == ":":
                        # print "Reaching"
                        dict_value = ""
                        elementLength = int(el)#int(ben[i])
                        i+=2
                        if i+elementLength == len(ben):
                            return "Something Wrong!"
                        else:
                            # print "Reaching"
                            # print "elementLength" + str(elementLength)
                            for x in range(i,i+elementLength):
                                dict_value += ben[x]
                            if past_key != "":
                                decoded_dict[past_key] = dict_value
                                # print decoded_dict
                                past_key = ""
                                key = True
                                i += elementLength
                                continue        
                            if key:
                                past_key = dict_value
                                key = False
                            i += elementLength
                elif ben[i] == "i" and ( ben[i+1] == "+" or ben[i+1] == "-" or RepresentsInt(ben[i+1])) and ben[i+1] != ":" and past_key != "":
                    bencoded_int = "i"
                    x = 0
                    if ben[i+1] == "+":
                        x = i + 2
                        bencoded_int += "+" 
                    elif ben[i+1] == "-":
                        x = i + 2
                        bencoded_int += "-"
                    else:
                        x = i + 1    
                        # print "X is: " + str(x)
                        # print ben[x]
                    while(RepresentsInt( ben[x] )):
                        # print "ben[x] in is:" + str(ben[x])
                        # print "x in is" + str(x)
                        x += 1    
                    # print ben[i]
                    to_decode = ben[i:x+1]
                    print to_decode + " value"
                    decoded_int = debencodeint(to_decode)
                    #return decoded_int
                    decoded_dict[past_key] = int(decoded_int)
                    # print decoded_dict
                    past_key = ""
                    key = True
                    i = x + 1
                    # print ben[i]
                    continue
                elif ben[i] == "d" and RepresentsInt(ben[i+1]) and ben[i+2] == ":" and past_key != "":
                    x = i
                    print x
                    while( True ):
                        if i == len(ben)-1:
                            break
                        elif ( ben[i] == "e" and ( ben[i+1] == "l" or ben[i+1] == "d" ) ):    
                            break
                        else:
                            print i,
                            i += 1
                    
                    # return "Nothing"
                    # print i,
                    # print ben[i]
                    # print i+1, ben[i+1]
                    # if RepresentsInt(ben[i])
                    to_decode = ben[x:i]
                    print to_decode
                    decoded_dict_value = debencodedict(to_decode)
                    # print decoded_dict_value
                    decoded_dict[past_key] = decoded_dict_value
                    # print decoded_dict
                    past_key = ""
                    key = True
                    if ben[i] == "e":
                        i += 2
                    else:
                        i += 1
                    continue
                elif ben[i] == "d" and ben[i+1] == "e" and past_key != "":
                    decoded_dict[past_key] = {}
                    #print decoded_dict
                    past_key = ""
                    key = True
                    i += 2
                    continue
                else:
                    return "Something Wrong 2!"    
            else:
                i += 1                                 
        return decoded_dict
                         
    else:
        return "Something Wrong 1!"   
            
        
def debencodeint(ben):
    decoded_integer = ""
    i = 1
    if ben[0] != "i" or ben[len(ben)-1] != "e":   
        return "Oops, Looks like you didnt send a bencoded int!"
    elif ben[0] == "i" and ben[1] == "e" and len(ben) == 2:
        return 0
    elif ben[1] == "+":
        decoded_integer = debencodeint(ben.replace("+",""))
        return int(decoded_integer)
    elif ben[1] == "-":
        decoded_integer += "-"
        decoded_integer += str(debencodeint(ben.replace("-","")))
        return int(decoded_integer)
    elif not RepresentsInt(ben[1]):
        return "There is no integer"
    elif RepresentsInt(ben[i]):
        while( RepresentsInt(ben[i]) ):
            decoded_integer += ben[i]
            i += 1
        if RepresentsInt(decoded_integer) and len(decoded_integer) == ( len(ben) - 2 ):
            return int(decoded_integer)
    else:
        return "Something Wrong!"
