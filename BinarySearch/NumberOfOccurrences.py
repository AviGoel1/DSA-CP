# Gfg Problem Link:- https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1/

def last(self,arr,l,h,x):
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
    
def first(self,arr,l,h,x):
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

def count(self,arr, n, x):
	i1 = self.first(arr,0,n-1,x)
	i2 = self.last(arr,0,n-1,x)
	if i1 == -1:
		return 0
  return i2-i1+1
