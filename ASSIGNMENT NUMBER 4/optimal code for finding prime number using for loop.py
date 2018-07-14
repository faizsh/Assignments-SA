no=int(input('Enter a number:'))
temp=no//2
for i in range(2,temp):
 if(temp%i==0):
     print('Number is not a prime number')
     break
if(i==temp-1):
    print('Number is prime number')
