nums = list(map(int, input("Enter elements of a list: ").split()))

nums2 = sorted(nums)
peak_ele = nums2[-1]
peak_index = nums.index(peak_ele)

print("Peak element is", peak_ele)
print("Peak element index:", peak_index)
