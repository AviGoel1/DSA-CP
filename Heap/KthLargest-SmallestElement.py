""" 
(kth Largest) Leetcode link:- https://leetcode.com/problems/kth-largest-element-in-an-array

(kth Smallest) Gfg Link:- https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1/
"""

def findKthLargest(nums,k):
        min_heap = []
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(k):
            heappush(min_heap,nums[i])
        for i in range(k,n):
            if min_heap[0] < nums[i]:
                heappop(min_heap)
                heappush(min_heap,nums[i])
        return min_heap[0]
      
def kthSmallest(nums, l, r, k):
        max_heap = []
        if r == 1:
            return nums[0]
        for i in range(k):
            heappush(max_heap,-nums[i])
        for i in range(k,r+1):
            if max_heap[0] < -nums[i]:
                heappop(max_heap)
                heappush(max_heap,-nums[i])
        return -max_heap[0]

nums = list(map(int,input().split(',')))
k = int(input())
print(findKthLargest(nums,k))
print(kthSmallest(nums, 0, len(nums)-1, k))
