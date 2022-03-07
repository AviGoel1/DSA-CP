# Gfg Problem Link:- https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x2041/1/
# Leetcode Link:- https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def last(arr,l,h,x):
  """ Here we are checking if element exists in upper half, if it is already found at an index. """
  res = -1
  while l <= h:
    m = l + (h-l)//2
    if arr[m] == x:
      res = m
      l = m+1
    elif arr[m] <= x:
      l = m + 1
    else:
      h = m - 1
  return res
    
def first(arr,l,h,x):
  """ Here we are checking if element exists in lower half, if it is already found at an index. """
  res = -1
  while l <= h:
    m = l + (h-l)//2
    if arr[m] == x:
      res = m
      h = m-1
    elif arr[m] >= x:
      h = m - 1
    else:
      l = m + 1
  return res

n = int(input())
arr = list(map(int,input().split()))
x = int(input())
print(first(arr,0,n-1,x))
print(last(arr,0,n-1,x))
