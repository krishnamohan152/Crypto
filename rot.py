a = input("Please Enter the String: ")
shift = input("Enter the rotations: ")
a = a.lower()
shift = int(shift)

dict_1 =  { 0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
#dict_2 = { 0:'z',1:'y',2:'x',3:'w',4:'v',5:'u',6:'t',7:'s',8:'r',9:'q',10:'p',11:'o',12:'n',13:'m',14:'l',15:'k',16:'j',17:'i',18:'h',19:'g',20:'f',21:'e',22:'d',23:'c',24:'b',25:'a'}

# Encryption

l = []
for i in a:
	p = (dict_1.items())
	space = ' '
	for w,w1 in p:
		if ( i == w1 and i != " "):
			num = (w+shift)%26
			space = dict_1.get(num)
		elif ( i == ""):
			space +=i
	l.append(space)



def listToString(l):
	str1 = ""
	for ele in l:
		str1 += ele
	return str1

enc = listToString(l)
print("The Encoded String is: "+enc)


# Decryption

l1 = []
for i in enc:
        p = (dict_1.items())
        space = ' '
        for w,w1 in p:
                if ( i == w1 and i != " "):
                        num = (w-shift+26)%26
                        space = dict_1.get(num)
                elif ( i == ""):
                        space +=i
        l1.append(space)



def listToString(l1):
        str1 = ""
        for ele in l1:
                str1 += ele
        return str1

dec = listToString(l1)
print("The Decoded String is: "+dec)




