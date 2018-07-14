no=int(input('Enter a number:'))
for i in range(2,no):
 if(no%i==0):
     print('Niumber is not a prime numbere')
     break
if(i==no-1):
    print('Number is prime number')
