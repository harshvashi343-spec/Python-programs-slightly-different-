#it counts your gene % in your decendents
n=1
b=1
c=2
j=0
d=int(input("generation number-: "))
for i in range (1,d+1):
	    if i<=1:
	    	n=1
	    	j=n*100
	    else:
	      	n=(n/c)
	      	j=n*100
	    	
	    print(i,". ",(("{:.1000000f}".format(j)).rstrip('0')).rstrip('.'),"%" )   	
print("the % of gean of the person after",d,"generations will be ")
print(n*100,"%")	    		    	
	  
	  