import collections
def longestPalindrome(s):
    ans = 0
    #Count the number of occurences of each item
    for v in collections.Counter(s).itervalues():
        ans += v / 2 * 2
        #check if odd add 1
        if ans % 2 == 0 and v % 2 == 1:
            ans += 1
    return ans
print(longestPalindrome("eeys"))