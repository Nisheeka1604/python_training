import math


def square():
    s=int(input("Enter the side length: "))
    return s * s


def rectangle(length, width):
    print("Area of Rectangle:", length * width)


def circle():
   r=int(input("Enter the radius: "))
   return 3.14 * r * r

def triangle(base, height):
    return 0.5 * base * height


def exit_program():
    print("Exiting the program.")

while True:
    print("Choose a shape:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        square()
    elif choice == 2:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        rectangle(length, width)
    elif choice == 3:
        x=circle()
        print("Area of Circle:", x)
    elif choice == 4:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        y=triangle(base, height)
        print("Area of Triangle:", y)
    elif choice == 5:
        break
