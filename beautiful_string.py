
# You are given a string, S, consisting of lowercase English letters.
# A string is beautiful with respect to S if it can be derived from S by removing exactly 2 characters.
# Find and print the number of different strings that are beautiful with respect to S .


# This problem is just counting how many ways there are to
# remove the two characters. For this, we can group the string
# by character, and after that either we remove two characters
# from two groups, or both from one group.
#
# There's one potential duplication we have to remove: if a group
# has size 1 and two groups around it have the same character
# (e.g. 'aaabaaaaa'), and we pick one from the middle group, it
# doesn't matter which of the two side groups we pick from, so
# we have to subtract 1 for each of this pattern.

import itertools

def count_beautiful(s):
	groups = [(k,len(list(v))) for k,v in itertools.groupby(s)]
	multiple = sum(x[1] > 1 for x in groups)
	fence = sum(groups[i - 1][0] == groups[i + 1][0] and groups[i][1] == 1 \
	            for i in range(1, len(groups) - 1))
	print(multiple + len(groups) * (len(groups) - 1) / 2 - fence)