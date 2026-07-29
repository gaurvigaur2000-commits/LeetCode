num = int(input("Enter number: "))
count, num2 = 0, num

while num:
    digit = num % 10

    if num2 % digit == 0:
        count += 1
    num //= 10

print("Count: ", count)

