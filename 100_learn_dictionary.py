""" counts = {}
data = [2,3,4,5,2,5,6,4]
for elem in data:
    counts[elem] = counts.get(elem, 0) + 1
for k in sorted(counts.keys(), reverse=True):
    print(k, counts[k]) """


""" counts={}
letters = ['e','a','e','b','a','e','c']
for elem in letters:
    counts[elem] = counts.get(elem, 0) + 1

print(counts) """


""" d = {"a": 5, "b": 2, "c": 9}
most = max(d, key=d.get)
least = min(d, key=d.get)

print(least,most) """


""" prices = {"apple": 2, "fig": 5, "banana": 3}

for k in sorted(prices.keys()):
    print(k, prices[k]) """