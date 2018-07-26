#WAP to check whether the given string is pallindrom or not(VVIMP)
class Palindrome:
    def pal(self,w):
        temp=w
        l=list(w)
        l.reverse()
        w="".join(l)
        if(temp==w):
            return 0
        else:
            return 1
w=input('Enter a word')
obj=Palindrome()
a=obj.pal(w)            
if (a==0):
    print('Its a palindrome')
else:
    print('Its not a palindrome')
