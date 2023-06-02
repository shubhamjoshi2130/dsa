# Given a string S consisting of lowercase English characters, determine if you can make it a palindrome by removing at most 1 character.

tacocats --> True  # tacocats --> tacocat
racercar --> True  # racercar --> racecar, racrcar
kbayak --> True  # kbayak --> kayak 
acbccba --> True # acbccba --> abccba
abccbca --> True # abccbca --> abccba

abcd --> False
btnnure --> False


def check_panindrome(string_in):
    return check_palindrome_helper(string_in,0,len(string_in),False)

def check_palindrome_helper(string_in,start_ind,end_idx,discripency):
    if (string_in[start_ind]!=string_in[end_idx]) and (not discripency):
        return check_palindrome_helper(string_in,start_ind+1,end_idx) or check_palindrome_helper(string_in,start_ind,end_idx - 1,True)
    elif discripency:
        return False
    return True    


tacocats
                    check_palindrome_helper(string_in,start_ind+1,end_idx)                                           check_palindrome_helper(string_in,start_ind,end_idx - 1,True)
t(0) --> s(7) ----->              (t(0) --> t(6))                                                           or                 (a[1] --> s[7])

# Let's recall from math the definition of dot product: given two vectors a and b, the dot product is a1*b1 + a2*b2 + ... + aN*bN.
# A sparse vector is a vector with most elements equal to zero - imagine a vector with millions of elements (or even infinite, as is the case for e.g. the Fourier Transform), but only ten thousand or so are nonzero. Now, a machine learning application loads many such vectors in memory (from a file or a database) and computes many such dot products.

a,b

a = [1,0,0,3,0,0,1]
b = [0,0,0,0,0,0,2]

a= [[0,1],[3,3],[6,-1]] ---> ma[0] =1 , ma[3] = 3,  ma[6] = -1


Space -  O(K+L)  , K is number of non-zero elements in a and 
          L is number of non-zero elements in b

Time - O (N) , where N is lenght of the vector

-- 1st
def multiply_sparse_vectors(a,b):
    ma = dict()
    mb = dict()
    for i in len(a):
        if a[i] != 0:
            ma[i] = a[i]
    del ma
    gc.collect()
    for i in len(b):
        if b[i] != 0:
            mb[i] = b[i]

    del mb
    gc.collect()
    dot_prod = 0

    for k in ma:
        dot_prod += ma[k] * mb.get(k,0)

    return dot_prod


-- 2st
def multiply_sparse_vectors(a,b):
    dot_prod = 0
    for i in len(a):
        if b[i]!=0 and a[i]!=0:
            dot_prod += b[i]*a[i]
    return dot_prod



a = [1,0,0,3,0,0,1]
b = [0,0,0,0,0,0,2]

Iterating vecor a and b:-
a[0] = 1 , b[0] =0 , dot_prod =0
a[1] = 0 , b[1] =0 , dot_prod =0
a[2] = 0 , b[2] =0 , dot_prod =0
a[3] = 3 , b[3] =0 , dot_prod =0
a[4] = 0 , b[4] =0 , dot_prod =0
a[5] = 0 , b[5] =0 , dot_prod =0
a[6] = 1 , b[6] =2 , dot_prod = 1*2 =2
