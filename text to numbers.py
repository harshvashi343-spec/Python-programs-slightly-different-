def ttn(n):
    
    di = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,"six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,"eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,"fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,"nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40,"fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,"one hundred":100, "thousand": 1000,"one thousand":1000}
    
    
    l = []
    v = []
    x = 0
    if type(n)==str:
    	c=n.split(" ")
    	l.extend(c)
    	if "and" in l:
    		l.remove("and")
    	#print(l)
    	for i in l:
    	    	if i=="":
    	    		continue 
    	    		# cause when I use recurssion their are chances that an empty string is their  as first index
    	    	else:
    	    		f = di.get(i)
    	    		v.append(f)
    else:
    	v=n
    #print(v)	    
    
    if 1000 in v and  v.index(1000)==2 :
       if len(v)==3:
       	x=(v[0]+v[1])*v[2]
       else:
       	x=(v[0]+v[1])*v[2]+ttn(v[v.index(1000)+1:])
       
    elif 1000 in v and  v.index(1000)==1:
    	if len(v)==2:
    	  x=v[0]*v[1]
    	else:
    		x=(v[0]*v[1])+ttn(v[v.index(1000)+1:])
    	
    else:
           if 100 in v and len(v) == 2:
           	x = v[0] * v[1]
           	return (x)
           elif 100 in v and len(v)>2:
           	x = (v[0] * v[1]) + ttn(v[v.index(100)+1:])
           	return(x)
           elif len(v) == 2:
           	x = v[0] + v[1]
           	return(x)
           else:
           	x = v[0]
           	return(x)
    return(x)
        
#a=input ("enter words-: ")
#k=ttn(a)
#print(k)