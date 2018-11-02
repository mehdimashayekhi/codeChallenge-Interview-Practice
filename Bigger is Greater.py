#https://www.hackerrank.com/challenges/bigger-is-greater/problem?h_r=internal-search
def biggerIsGreater(w):
    str_list = list(w)
    n=len(w)
    found=False
    #Iterate backwards over the string and look for a strictly lexographically decreasing substring
        # If the decreasing substring is ever broken (ie a lexographically bigger char comes after a lexographically smaller char)
        # Call the decreasing substring the suffix and the char that breaks the sequence the pivot
        # Swap the pivot with the next lexographically larger char in the suffix
        # Sort the suffix to be lexographically increasing
        # The finished string will be: the string before the pivot + the char swapped with the pivot + the sorted suffix
        # If a pivot is never found, then the string is already the largest lexograpical permutation
    for i in range(n-2,-1,-1):
        if str_list[i]<str_list[i+1]:
            found=True
            pivot_index=i
            pivot = str_list[pivot_index]
            break
    if not found:
        return "no answer"
    
    before_pivot = str_list[:pivot_index]
    suffix =  str_list[pivot_index+1:]
    for i in range(len(suffix)-1,-1,-1):
        if suffix[i]>str_list[pivot_index]:
            temp = pivot
            pivot = suffix[i]
            suffix[i] = temp
            break
    return "".join(before_pivot + [pivot] + sorted(suffix))