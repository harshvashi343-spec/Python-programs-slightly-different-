
def ntt(n):
    one=["zero","one","two","three","four","five","six","seven","eight","nine"]
    tw=["_","eleven", "twelve","thirteen", "fourteen","fifteen","sixteen","seventeen","eighteen","nineteen",]
    tens=[" ","ten","twenty", "thirty", "forty","fifty","sixty","seventy","eighty","ninety"]
    
    if n<10:
        return(one[n])
    elif 11<=n and n<20:
        n=n-10
        return(tw[n])
    elif 20<=n and n<100 or n==10:
         a=n//10
         b=n%10
         if b==0:
             return(tens[a])
         else:
             return(tens[a]+" "+one[b])
    elif 100<=n and n<1000:
          a=n//100
          b=n%100
          if b==0:
              return(one[a]+" hundred")
          else:
              return(one[a]+" hundred"+"  "+ntt(b))
    elif 1000<=n and n<10000:
          a=n//1000
          r=n%1000
          if r==0:
              return(one[a]+" thousand")
          else:
              return(one[a]+" thousand"+" "+ntt(r))
    
    elif 10000<=n and n<=100000:
          a=n//10000
          r=n%10000
          if r==0:
              return(tens[a]+"thousand")
          elif a==1 and r!=0:
              R=str(r)
              e=R[0]
              e=int(e)
              c=r-(e*1000)
              if c==0:
              	return(tw[e]+" "+'thousand')
              else:	
                  return(tw[e]+" "+"thousand"+" "+ntt(c))
          else:
              return(tens[a]+" "+ntt(r))
    elif 100000<=n and n<1000000:
          a=n//100000
          r=n%100000
          if r==0:
              return(one[a]+" lakh")
          else:
              return(one[a]+" lakh"+" "+ntt(r))
    
    elif 1000000<=n and n<=10000000:
          a=n//1000000
          r=n%1000000
          if r==0:
              return(tens[a]+"lakh")
          elif a==1 and r!=0:
              R=str(r)
              e=R[0]
              e=int(e)
              c=r-(e*100000)
              if c==0:
              	return(tw[e]+" "+'lakh')
              else:	
                  return(tw[e]+" "+"lakh"+" "+ntt(c))
          else:
              return(tens[a]+" "+ntt(r))
    else:
        return (" number out of range ")
v=int(input ("enter value -:"))
b=ntt(v)
print(b,type(b))



