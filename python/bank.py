balance = 0

def displaybalance():
    global balance
    print("Balance is",balance)

def deposit(money):
    global balance
    if money <= 0:
        print("Error")
        return
    balance += money

def withdraw(money):
    global balance
    if money <= 0 or money > balance:
        print("Error")
        return
    balance -= money

while True:
    displaybalance()
    solve = int(input("Input number 1-3 :"))

    if solve == 1:
        print("How much you want to deposit")
        dep = int(input())
        deposit(dep)

    if solve == 2:
        print("How much you want to withdraw")
        wit = int(input())
        withdraw(wit)
    
    if solve == 3:
        displaybalance()
        break
