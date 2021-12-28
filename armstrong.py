# 153; sum of 1 cube + 3 cube + 5 cube = 153
num = int(input("Enter a number:  "))
sum = 0
temp = num
while temp > 0:
    c = temp % 10 #checking for reminder
    sum += c**3 ## cubing the reminder value
    temp //= 10
if num == sum:
    print("armstrong number")
else:
    print("not armstrong number")
 