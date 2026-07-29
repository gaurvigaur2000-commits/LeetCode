st = input("Enter string: ")
st = st.strip()
st = st.split()
res = " ".join(st[::-1])

print(res)