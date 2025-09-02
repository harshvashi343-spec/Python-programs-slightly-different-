import random as r
d={'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
nc=0
combo=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
#to print game board
def pri(n):
		b=""
		for i in range (1,10):
			f=n.get(str(i))
			if i in [3,6,9]:
				b=b+'|'+str(f)+"|"
				print(b)
				b=""
			else:
				b=b+'|'+str(f)
# check win
def c_w(z):
		pl=[]
		sl=[]
		for i in z:
			f=z.get(str(i))
			if f in ["x","o"]:
				if f==p:
					pl.append(int(i))
				else:
					sl.append(int(i))
			else:
				continue 
		for t in combo:
			if set(t).issubset(set(pl)):
				return(1)
			elif set(t).issubset(set(sl)):
				return(2)
		return("•")	
			
while True:
	fn=""	
	ai=""
	fr=""
	p=""
	nc=0
	hq=d.copy()
	yn=input('enter your name-: ')
	e=input("friend or ai-: ")
	while True:
		p=input(' x or o -: ').lower()
		if p not in ["x","o"]:
			print("enter x or o only")
		else:
			break
	#assigning val to counterpart		
	if e=="friend":
		fn=input("enter your name -: ")
		fr = "o" if p=="x" else "x"
	else:
	 ai ="o" if p == 'x'  else  "x"
	
	while nc<10:
		pri(hq)
		# players turn
		while True:
			u=input(f"{yn} your turn select  num-: ")
			if u in hq:
				if hq[u] in ["x","o"]:
						print("spot is occupied ")
				else:
						hq[u]=p
						nc+=1
						break
			else :
				print ("select valid block")
		df=c_w(hq)
		if df ==1:
				pri(hq)
				print(f"{yn} won 🎉")
				break
		#check for draw
		if nc==9  :
					print ("draw")
					break	
		# friend or ai
		elif e=="ai":
			g=[]
			for i in hq:
				f=hq.get(i)
				if f not in ["x","o"]:
					g.append(i)
			#analysis by ai
			#win for ai
			ac=[]
			pc=[]
			for i in g :
				#check if ai win
				ax=hq.copy()
				ax[i]=ai
				zx=c_w(ax)
				ac.append(zx)
				#check if player wins 
				av=hq.copy()
				av[i]=p
				zp=c_w(av)
				pc.append(zp)
			if {2}.issubset(set(ac)):
					a1=g[ac.index(2)]
					hq[a1]=ai
					
			elif {1}.issubset(set(pc)):
					a2=g[pc.index(1)]
					hq[a2]=ai
					
			else:
					if hq.get("5")==5:
						hq["5"]=ai
	
					elif int(i) in [1,3,7,9]:
						hq[i]=ai
						
					elif int(i) in [2,4,6,8]:
						hq[i]=ai
						
			nc=nc+1
			df=c_w(hq)
			if df ==2:
						pri(hq)
						print("ai won 🎉")
						break
		elif e== "friend":
			while True:
				uk=input(f"{fn} your turn select  num-: ")
				if uk in hq:
						if hq[uk] in ["x","o"]:
							print("spot is occupied ")
						else:
							hq[uk]=fr
							nc+=1
							break
				else :
					print ("select valid block")
			df=c_w(hq)
			if df ==2:
				pri(hq)
				print(f"{fn} won 🎉")
				break				
	j=input("wana play again ? -: ").lower()
	if j not in ["y","yes"]:
		break