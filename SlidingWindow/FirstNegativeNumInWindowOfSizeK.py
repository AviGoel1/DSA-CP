"""
Problem Statement:- Given an array A[] of size N and a positive integer K, find the first negative integer for each and every subarray of size K.

Problem Link:- https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1

Constraints:-
1 <= n <= 10^6
1 <= k <= n
-10^9 <= arr[i] <= 10^9

Input format:-
First line contains the integer n.
Second line contains n space-separated integers, denoting the array elements
Last line contains k, denoting the size of subarray

TestCase:-
5
-8 2 3 -6 10
2

Output:- -8 0 -6 -6

Python Implementation:-
"""

n = int(input())
lst = list(map(int,input().split()))
k = int(input())
negative = []
ws = we = 0
ans = []
while we < N:
  if A[we] < 0:
    negative.append(A[we])
  if we - ws + 1 > K:
    if len(negative) != 0 and negative[0] == A[ws]:
      negative.pop(0)
    ws += 1
  if we - ws + 1 == K:
    if len(negative) != 0:
      ans.append(negative[0])
    else:
      ans.append(0)
  we += 1
print(ans)
  













