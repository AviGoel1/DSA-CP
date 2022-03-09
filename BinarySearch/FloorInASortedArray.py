""" Problem Statement:- Given a sorted array and a value x, the floor of x is the largest element in array smaller than or equal to x. Write efficient functions to find floor of x.

Problem Link:- https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1

TestCase:- 
5
1 2 4 5 6
3

Output:-
1 (Index of element of floor of x)
"""

def findFloor(arr,n,key):
    l = 0
    h = n-1
    while l<=h:
        mid = l + (h-l)//2
        if arr[mid] ==  key:
            return mid
        elif arr[mid] > key:
            h = mid-1
        else:
            l = mid+1
    return l-1

n = int(input())
arr = list(map(int,input().split()))
key = int(input())
print(findFloor(arr,n,key))
