# FOR LOOP
for index in range(7):
    print(index)

for index2 in range(11):
    print(index2)

for index3 in range(2,11):
    print(index3)

for even in range(2,11,2):
    print(even)

for odd in range(1,11,2):
    print(odd)

my_name='python'
for name in my_name:
    print(name)

cars=['toyota','BMW','jaguar','ferrari','rollse royce']
for x in cars:
    print(x)

names=('jane','nancy','john','james','done')
for y in names:
    print(y)

fruits=['apple','banana','mango','blue berry']
for f in fruits:
    if f=="mango":
        break
    print(f)

for k in fruits:
    if k=='mango':
        continue
    print(k)