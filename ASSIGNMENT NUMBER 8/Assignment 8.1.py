#WAP to get max and min value in a dictionary


D={}
D.setdefault('Math',input('Enter your marks for Math'))
D.setdefault('Chem',input('Enter your marks for Chem'))
D.setdefault('Phy',input('Enter your marks for Phy'))
D.setdefault('Mech',input('Enter your marks for Mech'))
D.setdefault('Java',input('Enter your marks for Java'))
print(D)
a=max(D.values())
b=min(D.values())
print('The maximum value from the above string is',a)
print('The minimum value from the above string is',b)

