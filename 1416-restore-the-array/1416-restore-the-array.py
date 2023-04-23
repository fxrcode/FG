class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s) 
        
        # memo on starting index
        @cache
        def dfs(idx):
            if idx == n: return 1
            if s[idx] == '0': return 0 
            num = count = 0
            for i in range(idx, n):
                num = 10 * num + (ord(s[i]) - ord('0'))
                if num > k:
                    break
                count += dfs(i + 1)
            return count % MOD 
            
        return dfs(0)