class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.set = set()

    def popSmallest(self) -> int:
        if self.set:
            ans = min(self.set)
            self.set.remove(ans)
            return ans
        else: 
            self.curr += 1
            return self.curr -1

    def addBack(self, num: int) -> None:
        if self.curr > num:
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)