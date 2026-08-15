import itertools

digits = input("Enter digits: ")
h_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

groups = [h_map[d] for d in digits]
print(groups)

combination = itertools.product(*groups)
res = ["".join(i) for i in combination]

print(res)