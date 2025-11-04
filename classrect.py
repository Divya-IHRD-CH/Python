class Rectangle:
    def area1(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
l1=int(input("Enter the length of rect1:"))
b1=int(input("Enter the breadth of rect1:"))
rect1=Rectangle()
rect1.area1(l1,b1)
print("Area of rect1 is:",rect1.area())
print("perimeter of rect1 is:",rect1.perimeter())
l2=int(input("Enter the length of rect2:"))
b2=int(input("Enter the breadth of rect2:"))
rect2=Rectangle()
rect2.area1(l2,b2)
print("Area of rect2 is:",rect2.area())
print("perimeter of rect2 is:",rect2.perimeter())
if(rect1.area()>rect2.area()):
    print("area of rect1 is greater")
else:
    print("area of rect2 is greater")
        
