counts = {}
data = [2,3,4,5,2,5,6,4]
for elem in data:
    counts[elem] = counts.get(elem, 0) + 1
for k in sorted(counts.keys(), reverse=True):
    print(k, counts[k])