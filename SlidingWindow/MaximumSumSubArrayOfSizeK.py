"""
Problem Statement:- You are given an array of n integers, and an integer K. You need to find the maximum sum of subarray of Size K.

Problem Link:- https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1/

Constraints:-
1 <= n <= 10^6
1 <= k <= n
-10^9 <= arr[i] <= 10^9


Input format:-
First line contains the integer n.
Second line contains n space-separated integers, denoting the array elements
Last line contains k, denoting the size of subarray

TestCase:-
7
2 5 1 8 2 9 1
3

Output:- 19

Python Implementation :- 
"""

n = int(input())
lst = list(map(int,input().split()))
k = int(input())
ws = we = 0
maxsum = currsum = 0
while we < n:
  currsum += lst[we]
  if we - ws + 1 > k:
    currsum -= lst[ws]
    ws += 1
  if we - ws + 1 == k:
    maxsum = max(maxsum,currsum)
  we += 1
print(maxsum)

