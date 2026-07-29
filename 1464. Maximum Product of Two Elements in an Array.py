arr = list(map(int, input("Enter elements of array: ").split()))
arr = sorted(arr)
max_prod = ((arr[-1])-1) * ((arr[-2])-1)

print("Product: ", max_prod)