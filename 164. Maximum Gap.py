nums = list(map(int, input("Enter elements: ").split()))

if len(nums) < 2:
    print("Single element, therefore no gap!!")

else:
    nums = sorted(nums)
    gap_lst = []

    for i in range(1,len(nums)):
        gap_lst.append(abs(nums[i-1] - nums[i]))

    print(max(gap_lst))

