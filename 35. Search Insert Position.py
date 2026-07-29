nums = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target element: "))

if target in nums:
    print(nums.index(target))

else:
    nums.append(target)
    nums = sorted(nums)
    print(nums.index(target))