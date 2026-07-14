num = int(input("Enter number: "))
set1 = set()
        
while num != 1 and num not in set1:
    set1.add(num)
    sum = 0

    while num:
        sum += (num % 10) ** 2
        num //= 10
        
    num = sum

print("True" if num==1 else "False")
