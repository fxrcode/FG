class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count, i = {}, 0
        for j, v in enumerate(fruits):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0: del count[fruits[i]]
                i += 1
        return j - i + 1