""" Problem Statement:- Given an array which is sorted, but after sorting some elements are moved to either of the adjacent positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1]. Write an efficient function to search an element in this array. Basically the element arr[i] can only be swapped with either arr[i+1] or arr[i-1]. 

Test Case:-
7
10 3 40 20 50 80 70
70

Output:- 
6
"""

def modifiedBinarySearch(arr,n,key):
  l = 0
  h = n-1
  while l<=h:
    m = l + (h-l)//2
    if arr[m] ==  key:
      return m
    elif m-1 >= l and arr[m-1] == key:
      return m-1
    elif m+1 <= h and arr[m+1] == key:
      return m+1
    elif arr[m] > key:
      h = m-2
    else:
      l = m+2
  return -1

n = int(input())
arr = list(map(int,input().split()))
key = int(input())
print(modifiedBinarySearch(arr,n,key))

