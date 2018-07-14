for no in range(1,1001):
 t=no
 s=0
 while(no!=0):
    r=no%10
    s=(s+(r**3))
    no=no//10
 if(s==t):
  print(s)
 
