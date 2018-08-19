#######question###############33
# Square Subsequences
# A string is called a square string if it can be obtained by concatenating two copies of the same string. 
# For example, "abab", "aa" are square strings, while "aaa", "abba" are not. Given a string, how many (non-empty) subsequences 
# of the string are square strings? A subsequence of a string can be obtained by 
# deleting zero or more characters from it, and maintaining the relative order of the remaining characters.

# example baaba ----> "bb", "baba" (twice), and "aa" (3 of them) are the square subsequences.

def solve_sub(string, size):
	s1 = string[:size]
	size1 = len(s1) + 1
	s2 = string[size:]
	size2 = len(s2) + 1
	# f[i][j] number of common subsequences for first i character of first string and first j character of second strong 
	f = [[0 for i in xrange(size2)] for j in xrange(size1)]

	for i in xrange(1, size1):
	  for j in xrange(1, size2):
	    if s1[i - 1] != s2[j - 1]:
	      f[i][j] = f[i - 1][j] + f[i][j - 1] - f[i - 1][j - 1]
	    else:
	      f[i][j] = f[i - 1][j] + f[i][j - 1] + 1

	# We can get the number of common subsequences between str[0,X-1] and str[X, stringLength-1] 
	# where the second subsequence contains position X, by doing this:
	# Let a be the number of common subsequences between str[0,X-1] and str[X, stringLength-1], and 
	# let b be the number of common subsequences between str[0,X-1] and str[X+1, stringLength-1]. Add a-b to the answer. 
	# (baiscally fixing the first character of second string to get distinct square subsequence)
	# or to make things easire we fix the last character of square subsequence in first string, that's why we return the following

	return f[len(s1)][len(s2)] - f[len(s1) - 1][len(s2)]

def SquareSubstring(string):
	NUMBER = 1000000007
    length = len(string)
    count = 0
    for i in xrange(length):
      count = (count + solve_sub(string, i))% NUMBER

    print ("count",count)
    return count	