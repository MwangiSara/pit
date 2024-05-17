# FUNCTIONS
def greet():
    print('hello world')

greet()
greet()
greet()

def simon():
    num1=40
    num2=30
    total=num1+num2
    print(total)

simon()
def sub(): #user defined function
    num3=60
    num4=30
    total2=num3-num4
    print(total2)

sub()
simon()
def modu():
    return 20 % 3
print(modu())

def exp():
    return 3**3 
print(exp())

def addition(x,y): #x and y are parameters
    sum=x+y
    return sum
addition(30,50) #50 and 30 are arguments , 30 is x and 50 is y
print(addition(30,50))
print(addition(100,150))
print(addition(66,54))

def multipy(one,two):
    return one*two
print(multipy(60,33))
print(multipy(44,5))

def sarah(a,b,c): #a,b,c are parameters
    return a*b*c
print(sarah(50,20,1,)) #50,20,1 are my arguments

def natalie(f,g,h):
    sum2=f+g+h
    # print(sum2)
    return sum2

natalie(30,77,45)
print(natalie(22,81,61))

def greeting(name):
    print(f"hello {name}, how are you?")

greeting("jane")
greeting("john")

def check(number):
    if number<=10:
        print("number is less than or equal to 10")
    else:
        print('number is more than 10')

check(4)
check(11)
check(50)
# nested function
def outer_function():
    """this is a docstring"""
    x=54
    def inner_function():
        print(x)
    inner_function()


outer_function()

# modules
import math
def area(radius):
    return math.pi*radius**2
print(area(14))

print(math.sqrt(9))
print(math.sqrt(81))
print(math.log(90))
print(math.factorial(4)) #4!=1*2*3*4

from math import log10
print(log10(202))





