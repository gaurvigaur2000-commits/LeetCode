s = "eettcode"
char_count = {}

for char in s:
    
    if char not in char_count:
        char_count[char]=1
    
    else:
        char_count[char]+=1

print("The first unique character is: ", end="")

for index, char in enumerate(s):
    
    if char_count[char]==1:
        print(index)
        
        break