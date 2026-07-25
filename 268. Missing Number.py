
li = [3, 4, 0, 1]
n = len(li)
exp_sum = n * (n+1) //2
sum_li = sum(li)
missing_val = exp_sum - sum_li
print(missing_val)