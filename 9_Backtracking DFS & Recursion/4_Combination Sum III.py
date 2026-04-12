## Combination Sum III

""" 
Find all valid combinations of k numbers that sum up to n such that:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations.

Input
A single line containing two integers k and n (2 ≤ k ≤ 9, 1 ≤ n ≤ 60).

Output
Print all valid combinations, one per line. Each combination is a sorted list of numbers separated by spaces. Print the combinations in lexicographic order.

Sample Input 1:
Copy
3 7
Sample Output 1:
Copy
1 2 4
The only combination of 3 numbers from 1-9 that sums to 7 is {1, 2, 4} (1+2+4=7).

 """

def solve():
    ## Take input
    k,n = map(int,input().split())
    res = []

    ## make a bactrack
    def bkt(start, path, remaining):
        if len(path) == k and remaining == 0:
            res.append(path[:])
            return
        if len(path)==k or remaining <= 0:
            return
        for i in range(start, 10):
            path.append(i)
            bkt(i+1, path, remaining-i)
            path.pop()
        
    bkt(1,[], n)

        ## loop the res and print sub sets
    res.sort()
    for sub in res:
        print(*sub)
solve()