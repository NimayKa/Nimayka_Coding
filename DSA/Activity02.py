import Activity02Stack as Sk

def dectobin(x):
    Reminder = Sk.stack()

    while x > 0:
        rem = x % 2
        Reminder.push(rem)
        x = x // 2

    bin_str=''

    while not Reminder.is_empty():
        bin_str += str(Reminder.pop())
    return bin_str
    
num1 = int(input("Please Input Decimal Number: \n"))
print(dectobin(num1))