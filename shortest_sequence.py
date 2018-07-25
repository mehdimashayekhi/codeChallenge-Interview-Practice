# Give an array A of n integers where 1 <= a[i] <= K. 
# Find out the length of the shortest sequence that can be constructed out of numbers 1, 2, .. k that is NOT a subsequence of A. 
# eg. A = [4, 2, 1, 2, 3, 3, 2, 4, 1], K = 4 
# All single digits appears. Each of the 16 double digit sequences, (1,1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2) ... appears. 
# Because (1, 1, 2) doesn't appear, return 3.

 
def shortestNonSeq(a, k):
        result = 0
        set_flag= Set()
        for i in range(len(a)):
            if (a[i] not in set_flag):
                set_flag_.add(a[i])
                if (len(set_flag)== k):
                    result+=1
                    set_flag= Set()

        return result + 1


# explanation:


# 1) If an input string S does not contain all K characters, then the answer is obviously 1, as any missing character forms a string that is not a substring of S 

# 2) Otherwise, an input string S can be represented as a concatenation S1 S2 where 
# S1 is the *shortest* prefix of S that contains all K characters and (a possibly empty) suffix S2. 

# Now, if the suffix S2 contains all K characters it can also be represented as a concatenation of a shortest prefix that contains 
# all K characters and (a possibly empty) suffix. 

# Repeating this process until we get a suffix that does not contain all K characters, an input string S can uniquely be represented 
# as a concatenation of S1 S2 .. Sn where Si (i in [1..n-1]) is the shortest prefix of the rest of S (to be more precise, of the suffix of 
#     S produced by taking S1 S2 .. Si-1 prefix off) containing all K characters, and Sn - is the (possibly empty) suffix that does not contain 
# all K characters (meaning some of K characters are not in Sn). 

# 3) Since Si is the shortest prefix with all K characters, its last character occurs 
# only once (otherwise this character could be omitted producing a shorter prefix with all K characters). 

# 4) This is how to build a string that is guaranteed to not be a sub-sequence of 
# S and also having minimum length among other strings having this property, meaning that any shorter string is necessarily a 
# sub-sequence of S: s1 s2 .. sn, where si (i in [1..n-1]) is the last character of Si, and sn is any of the K characters not present in Sn. 

# First, let's prove that any shorter sequence q1 q2 .. qk, k<n is a sub-sequence of S. This part is obvious since qi is in Si,

# since Si contains all K characters (i in [1..k]). 

# Now, let's prove that the string s1 s2 .. sn is not a sub-sequence of S. Let's assume otherwise. Since S1 contains s1 only 
# as the last character, either the whole s1 s2 .. sn is a subsequence of S2 .. Sn, or just s2 s3 .. sn is a subsequence of S2 .. Sn. 
# Either way, s2 s3 .. sn is a subsequence of S2 S3 .. Sn. Now, since S2 contains s2 only as the last character, s3 .. sn is a 
# subsequence of S3 .. Sn. By repeating this n-1 times we get that sn is a subsequence of Sn, but this cannot be true because sn was specifically 
# chosen as one of the K characters not in Sn. We get a contradiction which means s1 s2 .. sn is not a subsequence of S. 

# Now, having proved that s1 .. sn is the minimal string that is not a subsequence of S, we see that in order to compute n we just need to 
# break up the input string S into concatenations S1 .. Sn-1 Sn, as outlined in 2) and count the number of these. This is exactly what the algorithm is doing
    