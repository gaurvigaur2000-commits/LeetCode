nums = list(map(int, input("Enter elements: ").split()))

min_ele, max_ele = min(nums), max(nums)
miss_ele = []

for ele in range(min_ele, max_ele + 1):
    if ele not in nums:
        miss_ele.append(ele)

print(miss_ele)