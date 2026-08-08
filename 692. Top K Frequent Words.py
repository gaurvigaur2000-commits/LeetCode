words = list(input("Enter words: ").split())
k = int(input("No. of frequent words: "))
freq_words = {}

for word in words:

    if word not in freq_words:
        freq_words[word] = 1
    else:
        freq_words[word] += 1

sort_lst = sorted(freq_words, key=lambda x: (-freq_words[x], x))

res = sort_lst[:k]
print(res)