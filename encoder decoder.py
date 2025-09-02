import random as r
import ast
import json
l=[' ', '"', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '~', '`', '|', '•', '√', 'π', '÷', '×', '§', '∆', '€', '¥', '$', '¢', '^', '°', '=', '{', '}', '\\', '%', '©', '®', '™', '✓', '[', ']', '@', '#', '₹', '_', '&', '-', '+', '(', ')', '/', '?', '!', ';', ':', "'", '*','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
try:
	with open ("dictionary.json","r") as f:
	     d=json.load(f)
	     if not isinstance(d,dict):
	     	d={"use":{}}
	     
except (FileNotFoundError, json.JSONDecodeError):
    d = {"use":{}}
    
print('s -: show peoples, \nc -: generate key , \ncl -: clear every thing , \np -: add new person, \nps -: select key for person , \npd -: delete person , \ndd -: delete key from person (if you will add +del to person name no spacing it willclear all keys in person) , \ng -: give temporary  key to  encode or decode, \ngs -: save given key' )
u=input("-:  ").lower()
if u=="p":#add new person 
   p=input("enter new person -:").lower()
   if p not in d and p not in  d["use"]:
   	d[p]=[]
   	d['use'][p]=0
   else:
   	print(f"{p} exists in d")   	
elif u=='show':#it shows the persons
	h=[]
	for i in d:
		if i != 'use':
			h.append(i)
	print(h)
elif u=='cl':
	d={'use':{}}
elif u== 'ps':#it selects person code num
	o={}
	for i in d:
		if i != 'use':
				e=str(len(o)+1)
				o[e]=i
		else:
			continue	
	print(o)
	print(d.get('use'))
	n=int(input('enter persons number-: '))
	r=o.get(str(n))
	v=d.get(r)
	s={}
	ab=d['use'].get(r)
	for i in v:
	   	g=str(len(s)+1)
	   	s[g]=i
	print(r,s)
	a= int(input(" select code by entering num-: "))
	
	if a:
		a=a-1
		d['use'][r]=a
	else:
		d['use'][r]=ab			
elif u=='c':#new code will be generated automatocally"
	user=input(" you wana change the code ??").upper()
	if user=='Y':
		y=l.copy()
		r.shuffle(y)
		o={}
		for i in d:
			if i != 'use':
				e=str(len(o)+1)
				o[e]=i
			else:
					continue
		print(o)
		n=int(input('enter persons number-: '))
		r=o.get(str(n))
		d[r].append(y)	 
	else:
				print('invalid input')
elif u=='dd':
	t=[]
	for i in d:
		if i!='use':
			t.append(i)
	print(t)
	print("if want to delete all content in person add +del with the name ")
	delete=input(("enter person-: "))
	j=[]
	if delete in d :
		y=d.get(delete)
		g={}
		for i in y:
			x=len(g)+1
			g[str(x)]=i
		print(g)
		s=(input('enter num to delete : '))
		if s.isdigit():
			s=int(s)
			o=g.get(str(s))
			for i in y:
					if i != o:
						j.append(i)
					else:
						continue 
			d[delete]=j
		else:
			print('you skipped process no deleting')
	elif '+del' in delete:
		w=[]
		delete=delete.replace('+del','')
		if delete in d:
			d[delete]=w
		else:
			print(f'{delete} not found ')
	else:
		print(f'{delete} not found')
		
elif u=='pd':#delete existing person 
	w=[];
	for i in d:
		if i != 'use':
			w.append(i)
	print(w)
	de=input('enter person to del-: ')
	z={'use':{}}
	if de in d:
		for i in d:
			if i != de and i!='use':
				x=d.get(i)
				h=d['use'].get(i)
				z['use'][i]=h
				z[i]=x
			else:
				continue 
		d=z	
elif u=='g':#give unique code temp
	#temporary code change by user input
	user=input("enter list/string-: ")
	user=ast.literal_eval(user)
	g=user
elif u=='gs':#permanent code change by user input
	user=input("enter list/string-: ")
	user=ast.literal_eval(user)
	o={}
	for i in d:
		if i != 'use':
			e=str(len(o)+1)
			o[e]=i
		else:
			continue 
	print(o)
	n=int(input('enter persons number-: '))
	r=o.get(str(n))
	d[r].append(user)

with open ("dictionary.json","w") as f:
	    	json.dump(d,f)	
			
print(' (en) for encode (de) for decode ')
m=input("encode or decode ? ")
if m not in ['en','de']:
	print('invalid input ')
else:
	k=[]
	h=""
	for i in d:
		if i != 'use':
			k.append(i)
			print(k)		
	s=input("enter message-: ")	 	 
if  m=='en':
	 	 w=input("persons name-: ").lower()
	 	 if u=='g':
	 	 	for i in s:
	 	 	   try:
	 	 	            n=l.index(i)
	 	 	            h+=g[n]
	 	 	   except:
	 	 	   	if i not in l:
	 	 	   		continue 
	 	 	print(f'your encoded code is -: {h}')
	 	 elif w not in d:
	 	 	print("person not found")
	 	 else:
	 	 	q=d["use"].get(w)
	 	 	b=d.get(w)
	 	 	y=b[q]
	 	 	for i in s:
	 	 	       try:
	 	 	            	n=l.index(i)
	 	 	            	h+=y[n]
	 	 	       except:
	 	 	            	if i not in l:
	 	 	            		continue
	 	 	print (f"your code encoded -: {h}")	          	          		 
elif  m=='de':
	 	 w=input("persons name-: ").lower()
	 	 if u=='g' :
	 	 	for i in s:
	 	 	   try:
	 	 	            n=g.index(i)
	 	 	            h+=l[n]
	 	 	   except:
	 	 	   	if i not in l:
	 	 	   		continue 
	 	 	print(f'your decoded  code is -: {h}')
	 	 elif w not in d:
	 	 	print("person not found")
	 	 else:
	 	 	q=d["use"].get(w)
	 	 	b=d.get(w)
	 	 	y=b[q]
	 	 	for i in s:
	 	 	       try:
	 	 	            	n=y.index(i)
	 	 	            	h+=l[n]
	 	 	       except:
	 	 	            	if i not in l:
	 	 	            		continue
	 	 	print (f"your code encoded -: {h}")
else:
   print('no option selected ')
   
