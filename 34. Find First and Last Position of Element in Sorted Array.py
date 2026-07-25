lst = list(map(int,input("Enter elements: ").split()))
target = int(input("Enter element to find its first and last index: "))
fi, li = -1, -1

for i in range(len(lst)):
    if lst[i] == target:
        
        if fi == -1:
            fi = i
        li = i

print([fi, li])