#  Lets Look at a students scenario perfomance.
#  
marks = float(input('Enter Students Marks: '))
# marks = 78

if marks < 30:
    print("Below Average")

elif marks >=30 and marks < 40:
    print("Average")

elif marks >=40 and marks < 70:
    print("Above Average")

else:
    print("Excellent!")