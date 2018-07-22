#WAP a lambda function to get sum of 4 number use lambda function to impliment list
l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
l4=[10,11,12]
L=[x for x in map(lambda a,b,c,d:a+b+c+d,l1,l2,l3,l4)]
print(L)
