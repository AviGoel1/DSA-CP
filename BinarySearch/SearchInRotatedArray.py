# Problem Link :- https://leetcode.com/problems/search-in-rotated-sorted-array/

"""
Test Case:- 
4 5 6 7 0 1 2
0

Output:-
4
"""

# Approach :- Find how many times the array is rotated by finding the minimum element index (ind) then searching the element in the left half of the array from 0 to ind and then in right half from ind to n-1. As both these halves would be sorted individually, we will return the answer from that half where index returned is not -1.
# Left half for above Test Case :- (0-3) -> 4 5 6 7 || Right half for above Test Case:- (4-6) -> 0 1 2 || We can see both these halves are sorted individually.

def findRotation(nums,n):
  l = 0
  h = n-1
  while l<=h:
    m = (l+h)//2
    if nums[m] < nums[(m+n-1)%n] and nums[m] < nums[(m+1)%n]:
      return m
    elif nums[m] > nums[h]:
      l = m+1
    else:
      h = m-1
  return 0
    
def binarySearch(nums,l,h,target):
  while l<=h:
    m = (l+h)//2
    if nums[m] == target:
      return m
    elif nums[m] > target:
      h = m-1
    else:
      l = m+1
  return -1
    
def search(nums,target):
  n = len(nums)
  ind = findRotation(nums,n)
  ind1 = binarySearch(nums,0,ind-1,target)
  ind2 = binarySearch(nums,ind,n-1,target)
  return max(ind1,ind2)
