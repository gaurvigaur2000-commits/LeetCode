num = int(input("Enter a number: "))

sign = -1 if num < 0 else 1

num = abs(num)
reverse = int(str(num)[::-1])
final = sign * reverse

print(final)