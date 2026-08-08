arr = list(map(int, input("Enter elements of array: ").split()))
arr = sorted(arr)
dup_lst = []

for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        dup_lst.append(arr[i])

print(dup_lst)