nums = list(map(int, input("Enter elements: ").split()))
st = ""

for i in nums:
    st = st + str(i)

st = str(int(st)+1)
res_lst = []

for i in st:
    res_lst.append(int(i))

print(res_lst)

