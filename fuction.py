# ขอบเขตตัวแปร
balance = 1000
def displaybalance():
    print("Balance is",balance,"Baht")

def deposit(value):
    global balance
    money = value
    if money<=0:
        print("ไม่สามารถฝากเงินได้")
        return
    print("Deposit is",money,"Baht")
    balance += money

def withdraw(value):
    global balance
    money = value
    if money <=0 or money>balance :
        print("ไม่สามารถถอนเงินได้")
        return
    print("Withdraw is",money,"Baht")
    balance -= money

displaybalance()
withdraw(1000)
displaybalance()





'''
#lambda 

result = lambda base,n : base**n
print("Result =",result(3,2))

def check(num):
    if num % 2 == 0:
        return f"{num} is even"
    else :
        return f"{num} is odd"
def sum(*data):
    total = 0
    for item in data:
        total += item
    return total

print(sum(30,50,70))

number = int(input("Input number = "))
print(check(number))

def getCapital():
    return "กรุงเทพมหานคร"

def getPI():
    return 3.14

radius = int(input())
area = getPI()*radius**2
print("Area =",area)

def sayHello(time,name,age):
    print("สวัสดี",time,name)
    print("ปีนี้คุณมีอายุ",age,"ปี")

def showTable(num):
    for i in range(1,13):
        print(f"{num} x {i} = {num*i}")

# ข้อมูลแบบลำดับ *args
# ข้อมูลแบบกำหนดชื่อ **kwargs
def saveEmployee(**kwargs): #tuple
    print(f"ชื่อพนักงาน {kwargs["name"]}, แผนก {kwargs["department"]}")
    print(f"เงินเดือน {kwargs["salary"]} บาท")
    print(f"ที่อยู่ {kwargs["country"]}")

saveEmployee(name="ก้อง",department="ไอที",salary=40000,country="ภูเก็ต")
saveEmployee(name="ติน",department="หัวหน้า",salary=60000,country="ลพบุรี")
saveEmployee(name="เน็กซ์",department="แฟนหัวหน้า",salary=90000,country="ลพบุรี")


number = int(input())
showTable(number)

ti = input()
nam = input()
ag = input()
sayHello(ti,nam,ag)
'''