"""
Ak Yamin - 22FTT1344
DA3306 - Data Structures And Algorithms
"""
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
num1_advisor = []
num2_advisor = []
common = []
i = 1 
j = 1 

while i <= num1:
    if num1%i == 0:
        num1_advisor.append(i)
    i+=1

while j <= num2:
    if num2%j == 0:
        num2_advisor.append(j)
    j+=1

print ("Num1:",num1,":",num1_advisor)
print ("Num2:",num2,":",num2_advisor)

for i in num1_advisor:
    for j in num2_advisor:
        if i == j:
            common.append(i)
print("Common Divisor:",common) 

Greatest = max(common)
print ("GCD:",Greatest)