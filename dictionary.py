
d={'apple':1,'pear':2,3:'day'}
print(d['apple'])
print(d[3])
del d['pear']
d['b']=20
print(d)



def fun(a,b):
    print(a*b)
class balculator():
    def __init__(self,name,price,coulor,width,length,weight):
        self.name=name
        self.p=price
        self.c=coulor
        self.we=weight
    def add(self,x,y):
        print(self.name)
        result=x+y
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)
b=balculator('calculator',3,'red',3,4,5)
    
d['b']=b
print(d)

