start = int(input("Enter start value: "))
end = int(input("Enter end value: "))

odd_count = (end - start) // 2

if end % 2 == 1 or start % 2 == 1:
    odd_count += 1

print("Total odd numbers: ", odd_count)