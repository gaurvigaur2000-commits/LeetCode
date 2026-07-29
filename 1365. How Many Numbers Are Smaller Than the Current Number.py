nums = list(map(int, input("Enter elements of array: ").split()))
li = []

for i in range(len(nums)):
    count = 0

    for j in range(len(nums)):
        if nums[i] > nums[j] and i != j:
            count += 1
    li.append(count)

print(li)