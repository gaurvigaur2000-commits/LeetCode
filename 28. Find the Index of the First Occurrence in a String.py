st = input("Enter string: ")
sstr = input("Enter substring: ")

print(st.index(sstr) if sstr in st else "-1")