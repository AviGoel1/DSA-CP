""" Problem Statement:- Given a sorted array and a value x, the ceil of x is the smallest element in array greater than or equal to x. Write efficient functions to find ceil of x.

TestCase:- 
5
1 2 4 5 6
3

Output:-
4 (ceil of x)
"""

def findCeil(arr,n,key):
    l = 0
    h = n-1
    while l<=h:
        mid = l + (h-l)//2
        if arr[mid] ==  key:
            return arr[mid]
        elif arr[mid] > key:
            h = mid-1
        else:
            l = mid+1
    if l == -1:
        return "Ceil of x is not present in array"
    return arr[l]

n = int(input())
arr = list(map(int,input().split()))
key = int(input())
print(findCeil(arr,n,key))
