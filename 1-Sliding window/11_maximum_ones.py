n, k = map(int, input().split())
arr = list(map(int, input().split()))
left, maximumlength, count = 0,0,0

for right in range(n):
    if arr[right] == 0:
        count += 1
    
    while count > k:
        if arr[left] == 0:
            count -= 1
        left+=1
    maximumlength = max(maximumlength, right - left + 1)
print(maximumlength)