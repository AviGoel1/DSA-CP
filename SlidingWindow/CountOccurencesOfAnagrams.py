"""
Problem Statement:- Given a word pat and a text txt. Return the count of the occurences of anagrams of the word in the text.

Problem Link:- https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1

Constraints:-
1 <= |pat| <= |txt| <= 10^5


Input format:-
Single line containing two space separated strings pat and txt respectively.

TestCase:-
for forxxorfxdofr

Output:- 3

Explanation: for, orf and ofr appears in the txt, hence answer is 3.

Python Implementation:-
"""

from collections import Counter

k = len(pat)
hmap = Counter(pat)
ws = we = 0
count = 0
curr = {}
while we < len(txt):
  curr[txt[we]] = curr.get(txt[we],0) + 1
  if we - ws + 1 > k:
    curr[txt[ws]] -= 1
  if curr[txt[ws]] == 0:
    del curr[txt[ws]]
	  ws += 1
	if we - ws + 1 == k:
	  if len(curr) == len(hmap) and curr == hmap:
	    count += 1
	we += 1
return count







