# IF-ELIF-ELSE STATEMENT
number=0

if number>0: #condition 1
    print("positive number")
elif number==0: #condition 2
    print("zero")
else:
    print("negative number") #last option

marks=float(input('enter your marks'))

if marks<30:
    print("below average")
elif marks>=30 and marks<40:
    print("average")
elif marks>=40 and marks<70:
    print("above average")
else:
    print("excellent")
    if marks==100:
        print("valedictorian")
    else:
        print("invalid input")

# name="Jane"
# if len(name)>3:
#     print("caleb is more than 3")
# else:
#     print("caleb is less than 3")