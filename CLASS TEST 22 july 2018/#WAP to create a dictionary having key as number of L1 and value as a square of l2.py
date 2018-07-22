#WAP to create a dictionary having key as number of L1 and value as a square of L2l2
l1=[7,6,4]
l2=[2,3,5]
D={x:y for x,y in map(lambda a,b:(a,b**2) if a>b else (b,a**2),l1,l2)}
print(D)
