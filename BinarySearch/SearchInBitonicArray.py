""" Problem link :- https://www.geeksforgeeks.org/find-element-bitonic-array/

TestCase:-
7
-3, 9, 18, 20, 17, 5, 1
20

Output:-
3
"""

def findPeakElement(arr):
        n = len(arr)
        if n==1:
            return 0
        l = 0
        h = n-1
        while l <= h:
            m = l + (h-l)//2
            if m > 0 and m < n-1:
                if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                    return m
                elif arr[m-1] > arr[m]:
                    h = m-1
                else:
                    l = m+1
            elif m == 0:
                if arr[m] > arr[m+1]:
                    return 0
                else:
                    return 1
            elif m == n-1:
                if arr[m] > arr[m-1]:
                    return n-1
                else:
                    return n-2

def bsearch(arr,l,h,key):
  while l <= h:
    m = l + (h-l)//2 
    if arr[m] == key:
      return m
    elif arr[m] > key:
      h = m-1
    else:
      l = m+1
  return -1

def revbsearch(arr,l,h,key):
  while l <= h:
    m = l + (h-l)//2 
    if arr[m] == key:
      return m
    elif arr[m] < key:
      h = m-1
    else:
      l = m+1
  return -1
 
n = int(input())
arr = list(map(int,input().split(',')))
key = int(input())
ind = findPeakElement(arr)
ind1 = bsearch(arr,0,ind,key)
ind2 = revbsearch(arr,ind+1,n,key)
if ind1 == -1 and ind2 == -1:
  print('Element not present')
else:
  print(f'Element at index {max(ind1,ind2)}')


