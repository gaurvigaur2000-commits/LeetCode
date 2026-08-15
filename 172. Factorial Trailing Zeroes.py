num = int(input('Enter number: '))
count_zeroes = 0

while num:
    num = num//5
    count_zeroes += num

print("No. of trailing zeroes: ", count_zeroes)