#WAP to check Whether the given number is palindrom or not using function
def palindrome(no):
    rev,Value_user=0,no
    while(no!=0):
        r=no%10
        rev=rev*10+r
        no=no//10
    if(Value_user==rev):
        print('Number is palindrome')
    else:
        print('Number is not a palindrome')
no=int(input('Enter the syntax'))
palindrome(no)
