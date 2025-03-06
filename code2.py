score = int(input("Input Score = "))
grade = None

if score <= 100 and score >= 80 :
    grade = "A"
elif score <= 79 and score >= 70 :
    grade = "B"
elif score <= 69 and score >= 0 :
    grade = "F"
else :
    grade = "N (Invalid)"
    
print("You give",grade)







'''
print("Your score =",x)

if x<0 :
    print("ERROR")
elif x>=50 :
    print("PASS")
else :
    print("NOT PASS")

print("Number 1 =",number1)
print("Number 2 =",number2)
print("บวก =",number1+number2)
print("ลบ =",number1-number2)
print("คูณ =",number1*number2)
print("หาร =",number1/number2)
print("ยกกำลัง =",number1**number2)
print("หารไม่เอาจุดทศนิยม =",number1//number2)
print("เศษ =",number1%number2)

print(type(number1))
print(type(number2))
'''