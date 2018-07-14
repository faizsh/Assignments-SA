#WAP to take two guess input from user and predict whether he has guessed it correct or not.Give 4 chance to user.

i=1
import random
from random import randint

while(i<5):
 g1=int(input('enter the first number'))
 g2=int(input('enter the second number'))
 r1=print(random.randint(1,6))
 if(g1==r1 or g2==r1):
     print('Numbers are matched')
     i=5
 else:
     print('Numbers are not matched')
     i+1





 '''elif((g1 or g2)!=(r1 or r2)):
     print('Numbers are not matched')
 else:
     print('Enter the Number again')
 i=i+1'''
























'''for i in range(4):
 r=print(random.randint(1,6))
 if(g1==r):
    print('Entered number match')
 elif(g1!=r):
    print('Entered number doesnt match')
 elif(g2==r):
    print('Entered number match')
 elif(g2!=r):
    print('Entered number doesnt match')
 else:
     print('Enter the number again',i)'''



















'''for g1 in range(1,7):
    print('The entered number match',g1==r)
    print('The entered number doesnt match',g1!=r)
    break
for g2 in range(1,7):
    print('The entered numnber match',g2==r)
    print('The entered number doesnt match',g2!=r)
    break'''

















'''
while((g1 and g2)==(r1)):
    print('The entered number does match up',)
    break
    if((g1 and g2)!=r1):
     print('The entered numberr doesnt match up')
    else:
         print(g1,g2)'''
