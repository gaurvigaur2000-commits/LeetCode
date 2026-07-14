st = input("Enter string: ")
new_str=""

for i in st.lower():
    if i.isalnum():
        new_str+=i

print("True" if new_str==new_str[::-1] else "False")