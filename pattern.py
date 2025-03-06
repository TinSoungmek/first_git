# literal
'''
service = int(input())
match service:
    case 1 : print("ฝากเงิน")
    case 2 : print("ถอนเงิน")
    case 3 : print("สอบถามยอดคงเหลือ")
    case service : print(f"ไม่มีบริการหมายเลข {service} ในระบบ")
'''

# Guard Filter
'''
score = int(input())
print("score is",score)

match score :
    case 100 :
        print("Good")
    case score if score >= 50 and score < 100 :
        print("Pass")
    case _ :
        print("Not Pass")
'''

# OR
'''
data = input()
match data :
    case "เด็กชาย" | "นาย":
        print("เป็นเพศชาย")
    case "เด็กหญิง" | "นางสาว" | "นาง":
        print("เป็นเพศหญิง")
    case _ :
        print("ไม่พบข้อมูล")
'''

# Sequence 
'''
data = []
match data:
    case []:
        print("Not Found")
    case [1,2]:
        print("มีข้้อมูล 2 รายการ")
    case [1,2,3]:
        print("มีข้้อมูล 3 รายการ") 
'''

# Mapping
data = {"name" : "ติน","type" : "member"}

match data : 
    case {"type" : "member"}:
        print("คุณเป็นสมาชิกได้รับส่วนลด 50%")
    case _ :
        print("ไม่ได้รับส่วนลด")