arr1 = list(map(int, input("Enter elements of array 1: ").split()))
arr2 = list(map(int, input("Enter elements of array 2: ").split()))

arr1.extend(arr2)
arr1.sort()
print(arr1)
length = len(arr1)

if len(arr1)%2==1:
    median = arr1[length//2]

else:
    median = (arr1[(length//2)-1]+arr1[(length//2)])/2

print("Median: ", median)

