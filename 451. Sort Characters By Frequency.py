st = input('Enter string: ')
d = {}
for char in st:
    if char not in d:
        d[char]=1
    else:
        d[char]+=1

sort_d = sorted(d.items(), key=lambda x:(-x[1], x[0]))
for char, count in sort_d:
    print(char*count, end="")
        