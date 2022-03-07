"""
Optimization -> To prevent integer overflow, we calculate mid as:-

mid = low + (high-low)//2
"""

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

def bsearch_rec(arr,l,h,key):
  if l <= h:
    m = l + (h-l)//2
    if arr[m] == key:
      return m
    elif arr[m] > key:
      return bsearch_rec(arr,l,m-1,key)
    else:
      return bsearch_rec(arr,m+1,h,key)
  return -1

n = int(input())
arr = list(map(int,input().split()))
key = int(input())
print(bsearch(arr,0,n-1,key))
print(bsearch_rec(arr,0,n-1,key))
