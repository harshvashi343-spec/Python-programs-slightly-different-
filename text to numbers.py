def ttn(n):
    
    di = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,"six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,"eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,"fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,"nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40,"fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,"one hundred":100, "thousand": 1000,"one thousand":1000}

    l = []
    v = []
    c = n.split()
    l.extend(c)
    x = 0

    if "and" in l:
        l.remove("and")

    for i in range(len(l)):
        f = di.get(l[i])
        v.append(f)
        
    if 1000 in v and  v.index(1000)==2:
       if len(v) == 4  :
             x = (v[0] + v[1]) * v[2] + v[3]
             
       elif len(v) == 3 :
             x = (v[0] + v[1]) * v[2]
             
       elif len(v) == 5 and 100 in v:
           x = (v[0] + v[1]) * v[2] + ( v[3] * v[4])
       elif len(v) == 5 :
             x = (v[0] + v[1]) * v[2] + ( v[3] + v[4])
       elif len(v)==6  :
             x = (v[0] + v[1]) * v[2] + (v[3] * v[4]) +v[5]
       else:
             x = (v[0] + v[1]) * v[2] +(v[3] * v[4]) + v[5] + v[6]
    elif 1000 in v and  v.index(1000)==1:     
       if  len(v) == 4:
          x = (v[0] * v[1]) + (v[2] * v[3])
       elif  len(v) == 3:
          x = (v[0] * v[1]) + v[2]
       elif  len(v) == 5:
          x = (v[0] * v[1]) + (v[2] * v[3]) + v[4]
       elif  len(v) == 2:
          x = v[0] * v[1]
    
       else:
          x = (v[0] * v[1]) + (v[2] * v[3]) + v[4] + v[5]
    else:
       if 100 in v and len(v) == 2:
           x = v[0] * v[1]
       elif 100 in v and len(v) == 3:
           x = (v[0] * v[1]) + v[2]
       elif 100 in v and len(v)==1:
           x = v[0] 
       elif 100 in v:
           x = (v[0] * v[1]) + v[2] + v[3]
       elif len(v) == 2:
           x = v[0] + v[1]
       else:
           x = v[0]
    return(x)
        
a=input ("enter words-: ")
k=ttn(a)
print(k)