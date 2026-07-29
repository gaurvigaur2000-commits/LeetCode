num = int(input("Enter number: "))
product, total = 1, 0

while num:
    product *= num % 10
    total += num % 10
    num //= 10
    
print("Product:", product, " Sum:", total)
print("Difference between product and sum: ", product-total)