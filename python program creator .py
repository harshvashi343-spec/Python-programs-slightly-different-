#program.made using string manipulation 
class gv():
	use=[]
	def varc(self,b):#create variable 
		import random as r
		gx1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		y=""
		def qcx():
			while  True:
				qcx=r.choice(gx1)
				if qcx not in gv.use:
					gv.use.append(qcx)
					break
			return(qcx)
		if isinstance (b,list):
			for i in b:
				y=y+(qcx()+" = "+str(i)+"\n")
		else:
			y=qcx()+" = "+str(b)+"\n"
		return(y)
		
	def valc(self,v):#get numbers from data
		l=[]
		x=""
		for i in (v+"."):
			if i.isdigit():
				x=x+str(i)
			elif x.isdigit()==True and i.isdigit()==False:
				l.append(int(x))
				x=""
		return(l)
	def opr(self,v,u):
		q=""
		t=0
		joi=""
		ca=v.split()
		for i in gv.use:
			for i in ca:
				if i in ['add', '+', "sum"]:
						joi=" + "
						del ca[ca.index(i)]
						break
				elif i in ['multiply', '×']:
						joi=" * "
						del ca[ca.index(i)]
						break
				elif i in ['minus', '-', "subtract"]:
						joi=" - "
						del ca[ca.index(i)]
						break
				elif i in ['divide', '÷', "divide by ","division"]:
						joi=" / "
						del ca[ca.index(i)]
						break
						
			q=q+gv.use[t]+joi
			t+=1
		q=q[:(len(q)-2)]
		return(q)
		
	def stri(self,x):
		u=[]
		for i in x :
			u.append('"'+i+'"')
		return(u)

	def conc(self,v,y):
		h=""
		t=0
		for i in range(len(v)):
			h=h+gv.use[i]+"+"
		h=h[:-1]
		return (h)
		
	def loop(self,a):
			x=""
			def true():
				x="while True:"
				return(x)
			def fl(v):
				x="for i in "+v+" :"
				return(x)
			if a=="true":
				x=true()
			elif a=="fl":
				x=fl()
			else:
				x="errorr"
			return(x)
		
	def pri(self,g):
					g=g[:1]
					h="print( )"
					h=h.replace(" ",g)
					return(h)

#dont judge functions name as I didn't had any name so I gave random  where pro suggests program 

def proco ():				
	c=gv()
	v=input ("enter idea-: ")
	x=c.valc(v)
	y=c.varc(x)
	o=c.opr(v,y)
	z=c.varc(o)
	w=c.pri(z)
	print(f"{y}{z}{w}")

def procs ():
	y=""
	c=gv()
	v=input ("enter idea-: ")
	v=v.split(",")
	v=c.stri(v)
	y=c.varc(v)
	o=c.conc(v,y)
	z=c.varc(o)
	w=c.pri(z)
	print(f"{y}{z}{w}")
  
def plo():
	y=""
	c=gv()
	o=c.loop("true")
	print(o)		
				


			