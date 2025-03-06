# match statement
service = int(input("Input number(1-3) = "))

match service :
    case 1:print("Withdraw")
    case 2:print("Deposit")
    case 3:print("Money")
    case _:print("Error")












'''
username = input("Input username = ")
password = input("Input password = ")

if username == "member" and password == "1234" :
    print("Login")
    service = input("Input number(1/2) = ")
    if service == "1":
        print("Withdraw")
    elif service == "2":
        print("Deposit")
    else:
        print("Error")
else :
    print("Can't found")
'''