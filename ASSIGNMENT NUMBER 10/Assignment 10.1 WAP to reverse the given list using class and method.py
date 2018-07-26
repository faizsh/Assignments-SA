#WAP to reverse the given list using class and method

'''class Reverse:
    def rev(self,a):
        a.reverse()
        print(a)
obj=Reverse()
a=[(input('Enter the number')),(input('Enter the number')),(input('Enter the number')),(input('Enter the number')),(input('Enter the number')),(input('Enter the number')),]
print(obj.rev(a))'''







class Reverse:
    def rev(self,a):
        b=[]
        for i in range(len(a)):
            x=a[(len(a)-1)-i]
            b.append(x)
        return b
a=[int(input('Enter the number')),int(input('Enter the number')),int(input('Enter the number')),int(input('Enter the number')),int(input('Enter the number')),int(input('Enter the number')),]
obj=Reverse()
ans=obj.rev(a)
print(ans)
        
