start = int(input("start = "))
end = int(input("end = "))

for i in range(start,end+1):
    for j in range(1,13):
        print(i,"x",j,"=",i*j)
    print(" ")





'''
sum = 0 

while True:
    number = int(input()) 
    if number < 0:
        break
    sum += number
print(sum)


sum = 0
for i in range(1,6):
    number = int(input("ลำดับที่ "+str(i)+" = "))
    sum += number
print(sum)




number = int(input())
for count in range(1,13):
    print(number,"x",count,"=",count*number)
 



count = 0
while count<3:
    count+=1
    print(count)
'''