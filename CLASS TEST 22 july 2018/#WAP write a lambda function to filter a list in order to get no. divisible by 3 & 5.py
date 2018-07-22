#WAP write a lambda function to filter a list in order to get no. divisible by 3 & 5
l=[1,3,5,10,12,15,18,20,21,30]
L=[x for x in filter(lambda l:True if l%3==0 and l%5==0 else False,l)]
print(L)
