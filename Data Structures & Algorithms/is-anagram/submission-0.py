class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        elif len(s) != len(t):
            return False
        else:
            freq_s = {}
            freq_t = {}

            for index in range(len(s)):
                freq_s[s[index]] = freq_s.get(s[index], 0) + 1
                freq_t[t[index]] = freq_t.get(t[index], 0) + 1

            for k,v in freq_s.items():
                if k not in freq_t:
                    return False
                if freq_t[k] != v:
                    return False
                
            return True