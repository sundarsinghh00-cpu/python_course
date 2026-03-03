for i in range(20,-1,-5):
    print(i,end="")

for i in range(1,6):
    print(str(i)*i)

for i in range(1,5):
    print(str(i)*i)

count =0
for i in range(1,51):
    if i % 6 ==0 and i % 7 ==0:
        count+=1
        print(count)

count=0
for i in range(1,11):
    if i % 3== 0 and i % 6==0:
        count +=1 
        print (count)


vasshi = sum ( ko for ko in range(1,101)if ko % 4==0)
print(vasshi)

i=[1,2,3,4,5,6]
for i in i:
    print(i)

x="7"
y=3
print(x*y+"2")

x=5
print(2+x*3**2)

x=-17
y=5
print(x//y)
print(x/y)
print(x>5 and y <-17 or x==5)


