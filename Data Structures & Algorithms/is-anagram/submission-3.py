class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same length
        if (len(s) == len(t)):
        # same number of characters
            true_length = len(s)
            char_check = s + t
            seen = {}
            # the count of each character in s should double by the end of the t
            for i in range(len(char_check)):
                if char_check[i] not in seen:
                    seen[char_check[i]] = 0
                if i < true_length:
                    seen[char_check[i]] += 1 
                if i >= true_length:
                    seen[char_check[i]] -= 1
                if seen[char_check[i]] == 0:
                    del seen[char_check[i]]
            if not seen:
                return True
            
        return False
    
            # now we'll have a dictionary with counts            