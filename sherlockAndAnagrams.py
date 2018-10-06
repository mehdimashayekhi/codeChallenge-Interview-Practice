##############Question##################3
#Two strings are anagrams of each other if the letters of one string can be rearranged 
#to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
# e.g., ifailuhkqq --->there are three anagram pairs [i,i].[q,q],[ifa,fai]
# kkkk ---> there are 10 anagram pairs
def sherlockAndAnagrams(s):
    map_=collections.defaultdict(int)
    len_=len(s)
    #store all substrings in map
    for i in range(len_):
        for j in range(i,len_):
            map_[''.join(sorted(s[i:j+1]))]+=1
    res=0
    # choose 2 of n
    for k,v in map_.iteritems():
        res+=(v*(v-1))/2
    return res