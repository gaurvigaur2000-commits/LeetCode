num = int(input("Enter number: "))
lst = []

while num:
    digit = num % 10
    lst.append(digit)
    num //= 10

lst = sorted(lst)

print("Max product: ", lst[-1] * lst[-2])