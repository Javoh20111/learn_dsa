""" 
There are n applicants and m apartments. Each applicant desires an apartment size, and an apartment is acceptable if its size differs by at most k from the desired size. Each apartment can be given to at most one applicant. Find the maximum number of applicants that can get an apartment.

Input
The first line contains three integers n, m, and k (1 <= n,m <= 2*10^5, 0 <= k <= 10^9). The second line contains n integers a_i (desired sizes). The third line contains m integers b_i (apartment sizes). Each size satisfies 1 <= a_i,b_i <= 10^9.

Output
Print the maximum number of matches.

Sample Input 1:
4 3 5
60 45 80 60    45,60,60,80   <-- appartment
30 60 75       30,60,70      <-- aplicant
Sample Output 1:
2
Two applicants can be matched within tolerance.
 """

n1,n2,target = map(int,input().split())
aplicants = list(map(int,input().split()))
apartments = list(map(int,input().split()))

def sorter(aplicants, apartments):
    aplicants.sort()
    apartments.sort()
    return find_correct(n1, n2, target, aplicants, apartments)

def find_correct(n1, n2, target, aplicants, apartments):
    checker1 = 0
    checker2 = 0
    count = 0
    while checker1 <= n1 - 1 and checker2 <= n2 - 1:
        if apartments[checker2] < aplicants[checker1] - target:
            checker2+=1
        elif apartments[checker2] > aplicants[checker1] + target:
            checker1+=1
        else:
            count+=1
            checker2+=1
            checker1+=1
    return count
print(sorter(aplicants, apartments))
