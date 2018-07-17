#Using user define function WAP to find whether the given number is armstrong or not

def Armstrong(no):
    t=no
    s=0
    while(no!=0):
        r=no%10
        s=(s+(r**3))
        no=no//10
    return s==t
n=int(input('Enter the number:'))
if(Armstrong(n)):
    print('Number is armstrong number')
else:
    print('Number is not an armstrong number')



'''OR the other logic is

def Armstrong(no):
    t=no
    s=0
    while(no!=0):
        r=no%10
        s=(s+(r**3))
        no=no//10
    return s
n=int(input('Enter the number:'))
a=Armstrong(n)
if(Armstrong(n)==n):
    print('Number is armstrong number')
else:
    print('Number is not an armstrong number')'''

