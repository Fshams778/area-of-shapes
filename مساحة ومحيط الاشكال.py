print(" \n 1-square \n 2-circle \n 3-rectangle")
choice=int(input("enter the shape:"))

class Square:
    high=float(input("Enter the hight of the square:"))
    def __init__(self,high):
     self.high=high
     aria=self.high*self.high
     circumference=self.high*4
     print(f" The aria is: {aria}\n The circumference: {circumference}")

class Circle:
    redius=float(input("enter the redius:\n "))
    aria=3.14*redius*redius
    circumference=2*redius*redius
    print(f" The aria is: {aria}\n The circumference: {circumference}")

class Rectangle:
    high=float(input("Enter the hight of the rectangle:"))
    width=float(input("Enter the width of the rectangle:"))
    aria=high*width
    circumference=2*(high+width)
    print(f" The aria is: {aria}\n The circumference: {circumference}")

if choice==2:
    square=Square()
elif choice==2:
    circle=Circle()
else:
    rectangl=Rectangle()