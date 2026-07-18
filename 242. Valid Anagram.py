st1 = input("Enter string 1: ")
st2 = input("Enter string 2: ")

st1 = sorted(st1)
st2 = sorted(st2)

print("Anagram" if st1 == st2 else "Not Anagram")