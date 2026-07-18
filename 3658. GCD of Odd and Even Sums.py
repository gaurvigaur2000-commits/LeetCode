n = int(input("Enter n: "))
sum_odd, sum_even = 0, 0

for i in range(1, 2*n+1):
    
    if i%2==0:
        sum_even+=i
    
    else:
        sum_odd+=i

while sum_odd!=0:
    sum_even, sum_odd = sum_odd, sum_even % sum_odd

print("GCD of sum of even and odd numbers: ", sum_even)