class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        ans = cnt = 0
        for i, c in enumerate(s):
            if c in vowels:
                cnt += 1
            if i >= k and s[i - k] in vowels:
                cnt -= 1
            ans  = max(cnt, ans)
        return ans    