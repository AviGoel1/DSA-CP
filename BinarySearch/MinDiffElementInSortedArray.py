""" Problem Statement:- You are given an sorted array and an integer key. You need to return an element from the array whose absolute difference with the key is minimum.

Testcase:-
4
1 4 6 10
7

Output:-
6 {as abs(6-7) is minimum}
"""

# Approach :- This problem is a combination of two other variation of binary search problem i.e. floor and ceil of an element. So, we just need to find the floor and ceil of the given key and find the minimum absolute difference.

def minidiff(arr,n,key):
  l = 0
  h = n-1
  while l<=h:
    m = l + (h-l)//2
    if arr[m] == key:
      return key
    elif arr[m] > key:
      h = m-1
    else:
      l = m+1
  if abs(arr[l-1]-key) <= abs(arr[l]-key):
      return arr[l-1]
  else:
      return arr[l]

n = int(input())
arr = list(map(int,input().split()))
key = int(input())
print(minidiff(arr,n,key))
