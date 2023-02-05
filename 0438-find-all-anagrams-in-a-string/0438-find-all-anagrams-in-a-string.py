class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)
        
        ans = []
        l = 0
        for r, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:  # If number of characters `c` is more than our expectation
                cnt[s[l]] += 1  # Slide left until cnt[c] == 0
                l += 1
            if r - l + 1 == len(p):  #  If we already filled enough `p.length()` chars
                ans.append(l)  # Add left index `l` to our result
                
        return ans