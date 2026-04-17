from collections import Counter
s = input().strip()
con_s = Counter(s)

maxed = 0
sorted_dict = dict(sorted(con_s.items(), key=lambda item: item[1]))
print(sorted_dict[-1])
