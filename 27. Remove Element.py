nums = list(map(int, input("Enter elements: ").split()))
val = int(input("Enter value: "))

for i in reversed(nums):
    if i == val:
        nums.remove(val)

print("No. of elements which are not equal to val:", len(nums))
