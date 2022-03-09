# Problem Link:- https://practice.geeksforgeeks.org/problems/rotation4723/1/


""" 
Test Case:- 
5
3 4 5 1 2

Output:-
3
"""

def findKRotation(arr,  n):
    l = 0
    h = n-1
    while l<= h:
        m = (l+h)//2
        if arr[m] < arr[(m+n-1)%n] and arr[m] < arr[(m+1)%n]:
            return m
        elif arr[m] > arr[h]:
            l = m+1
        else:
             h = m-1
    return 0

n = int(input())
arr = list(map(int,input().split()))
print(findKRotation(arr,n))



