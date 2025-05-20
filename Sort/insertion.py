# Python program to find the longest substring
# with k unique characters in a given string

def longestkstr(s, k):
    n = len(s)
    answer = -1
    for i in range(n):
        for j in range(i+1, n+1):
            dict = set (s[i:j])
            if len(dict) == k:
                answer = max(answer,j-i)
    print(answer)
    
s = "aabbccc"
k = 3
longestkstr(s, k)
            