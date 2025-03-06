
try:
    num1 = int(input("number1 = "))
    num2 = int(input("number2 = "))
    if num1<0 or num2<0:
        raise Exception("ข้อมูลตัวเลขต้องเป็นค่าบวก")
    result = num1/num2
    print("Result =",result)
except ValueError:
    print("ข้อมูลไม่ถูกต้อง ป้อนเลขเท่านั้น")
except ZeroDivisionError:
    print("อย่าหารด้วย 0")
finally:
    print("End Program")