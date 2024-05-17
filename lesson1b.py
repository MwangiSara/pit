# arithmetic operations
sum=50+20
print(sum)
num1=50
num2=20
add=num1+num2
print(add)
sub=num1-num2
print(sub)
mul=num1*num2
print(mul)
divi=num1/num2
print(divi)
mol=num1%num2
print(mol)
exp=num1**num2
print(exp)

# simple interest
principle=2000
rate=12
time=4
interest=(principle*rate/100*time)
print(interest)

# area of a cone - 1/3*pie*r**2h

pie=3.142
radius=14**2
height=20

area=(1/3*pie*radius*height)
print(area)

# CI = p(1+r/100)^n

principle=2000
rate=10/100
n=5
CI=principle*(1+rate)**n
total=CI-principle
print(total)

x=10.0
y=(x<100.0) and isinstance(x,float)
print(y)