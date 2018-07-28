#WAP to take radius,lenght,breadth from user and find area of circle and rectangle using keyword argument.


class Area:
    def __init__(self,R=None,L=None,B=None):
        a=3.14*R**2
        b=L*B
        print('The area of the circle is',a,'cm^2')
        print('The are of the Rectangle is',b,'cm^2')

r,l,b=int(input('Enter the radius in cm : ')),int(input('Enter the lenght in cm: ')),int(input('Enter the breadth in cm: '))
obj=Area(r,l,b)
