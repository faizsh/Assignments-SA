#Operator Overloading multiplication

class operat:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __mul__(self,other):
        return(self.x*other.x+5,self.y*other.y+5)
ob1=operat(5,6)
ob2=operat(2,3)

print(ob1*ob2)
