""" Problem Link:- https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1/

TestCase:-
4
12,34,67,90
2

Output:-
113
"""

def isvalid(A,N,M,mid):
    s = 1
    curr = 0
    for i in A:
    curr += i
    if curr > mid:
        s += 1
        curr = i
    if s > M:
        return False
    return True
    
def findPages(A, N, M):
    if N < M:
        return -1
    l = max(A)
    h = sum(A)
    res = -1
    while l<=h:
        mid = l + (h-l)//2
        if isvalid(A,N,M,mid):
            res = mid
            h = mid-1
        else:
            l = mid+1
    return res

n = int(input())
arr = list(map(int,input().split(',')))
m = int(input())
print(findPages(arr,n,m))
