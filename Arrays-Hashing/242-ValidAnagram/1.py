# I used two hash tables to count the number os letters in each string.
# then compared the two arrays, and if they are the same, it means they are a anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        arr1 = [0] * 26
        arr2 = [0] * 26

        for i in range(len(s)):
            arr1[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            arr2[ord(t[i]) - ord('a')] += 1

        if( arr1 == arr2 ):
            return(True)
        
        return(False)