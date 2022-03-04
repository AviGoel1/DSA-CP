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
matched = 0
ws = we = 0
count = 0
while we < len(txt):
	if hmap.get(txt[we],None) != None:
		hmap[txt[we]] -= 1
		if hmap[txt[we]] == 0:
			matched += 1
	if we - ws + 1 > k:
		if hmap.get(txt[ws],None) != None:
			hmap[txt[ws]] += 1
		if hmap[txt[ws]] == 1:
			matched -= 1
		ws += 1
	if we - ws + 1 == k:
		if matched == len(hmap):
			count += 1
	we += 1
return count







