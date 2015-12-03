def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
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
        for i,char in enumerate(ben):
            if i != 0 and i != len(ben)-1:
                if RepresentsInt(char) and ben[i+1] == ":":
                    listElement = ""
                    elementLength = int(char)
                    i+=2
                    if i+elementLength == len(ben):
                        return "Something Wrong!"
                    else:
                        # print "Element Length: "+str(elementLength),
                        # print ",Element is: ",
                        for x in range(i,i+elementLength):
                            # print ben[x],
                            listElement+=ben[x]
                        decoded_list.append(listElement)    
                        # print "\n"    
                        i += elementLength
        return decoded_list                    

def debencodedict(ben):
    decoded_dict = {} #an empty dict
    if ben[0] == "l" and ben[len(ben)-1] == "e" and len(ben) == 2:
        return decoded_dict
        #print decoded_dict
    elif ben[0] != "l" or ben[len(ben)-1] != "e":
        return "Oops, Looks like you didnt send a bencoded dict!"
        #print "Oops, Looks like you didnt send a bencoded dict!"
    elif ben[0] == "l" and ben[len(ben)-1] == "e" and len(ben) > 2:
        
    else:
        return "Something Wrong!"   
            
        
    