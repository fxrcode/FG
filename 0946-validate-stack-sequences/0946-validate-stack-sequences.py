class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        r = 0
        stk = []
        for x in pushed:
            stk.append(x)
            while stk and r < len(popped) and stk[-1] == popped[r]:
                stk.pop()
                r += 1
        return r == len(popped)