#WAP a function to get sum of 4 number use user def function to impliment list
def sum(a,b,c,d):
    return a+b+c+d
l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
l4=[10,11,12]
L=[x for x in map(sum,l1,l2,l3,l4)]
print(L)
