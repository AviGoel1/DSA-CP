""" Problem Statement:- You are given a sorted array of alhpabets and an alphabet. You need to find the next letter of this alphabet present in the array if it exists. 

TestCase1:-
4
a c f h
c

Output:-
f

TestCase2:-
4
a c f h
g

Output:-
h
"""

def nextLetter(arr,n,key):
    l = 0
    h = n-1
    while l<=h:
        mid = l + (h-l)//2
        if arr[mid] ==  key and mid+1 != n:
            return arr[mid+1]
        elif arr[mid] > key:
            h = mid-1
        else:
            l = mid+1
    if l == n:
        return "Letter doesn't exist"
    return arr[l]

n = int(input())
arr = input().split(',')
key = input()
print(nextLetter(arr,n,key))
