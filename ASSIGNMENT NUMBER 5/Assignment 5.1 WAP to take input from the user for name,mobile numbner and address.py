#WAP to take input from the user for name,mobile numbner and address
a=(input('Enter the name:'))
b=(input('Enter the mobile number:'))
c=(input('Enter the address:'))
if(a.isalpha()):
    print('the provided name is correct',a)
else:
     print('Enter the name again please')

if(b.isdigit()):
    print('THe entered mobile number is verified',b)
else:
    print('Enter the mobile number again')
        
if(c.isalnum()):
    print('the address is verified',c)
else:
    print('Enter the address again')
 
