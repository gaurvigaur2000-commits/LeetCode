nums = list(map(int, input("Enter elements: ").split()))
print(nums)
target = int(input("Enter target: "))

i = 0
while i < len(nums):

    j = i + 1
    while j < len(nums):

        if nums[i] + nums[j] == target:
            ind1, ind2 = i, j
        j += 1
    i += 1

if "ind1" not in locals():
    print("No match found!!")
    
else:
    print([ind1, ind2])