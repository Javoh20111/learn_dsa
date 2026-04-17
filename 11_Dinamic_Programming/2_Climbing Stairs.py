## 2. Climbing Stairs

""" 
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Since the answer can be very large, print it modulo 10^9 + 7 (1000000007).

Input
A single integer n (1 ≤ n ≤ 10^6).

Output
Print the number of distinct ways to climb to the top, modulo 10^9 + 7.

Sample Input 1:
Copy
4
Sample Output 1:
Copy
5
There are 5 distinct ways to climb a staircase with 4 steps:

Copy
Way 1: 1+1+1+1          Way 2: 1+1+2            Way 3: 1+2+1

Step 4: ___*             Step 4: ___*             Step 4: ___*
Step 3: __*|             Step 3: __*|             Step 3: __*|
Step 2: _*||             Step 2: _*_|             Step 2: _*_|
Step 1: *|||             Step 1: *|__|             Step 1: *|__|
Ground: ||||             Ground: |__|             Ground: |___|
        ^1 at a time          1,1,then 2              1,2,then 1

Way 4: 2+1+1            Way 5: 2+2

Step 4: ___*             Step 4: ___*
Step 3: __*|             Step 3: __|_|
Step 2: _|_|             Step 2: _*__|
Step 1: _|__|            Step 1: _|___|
Ground: *___|            Ground: *____|
        2,then 1,1              2, then 2
 """
def find_comb(n,mod):
    count = [0] * (n + 1)
    count[0] = 1
    count[1] = 2

    for i in range(2, n+1):
        count[i] = (count[i-2] + count[i-1])%mod
    print(count[n-1])
n = int(input())
mod = 10**9 + 7
find_comb(n, mod)