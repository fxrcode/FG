class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def find(x):
            while x in pa:
                if pa[x] in pa:#path compress
                    pa[x]=pa[pa[x]]
                x=pa[x]
            return x    
        def union(x,y):
            pax,pay=find(x),find(y)
            if pax==pay:#union fail,has been unioned.
                return False
            pa[pax]=pay
            return True
        seen,pa,res,count=set(),{},[],0
        for x,y in positions:#connect with neighbor val==1,if union success,means one island disappear.
            if (x,y) not in seen:
                seen.add((x,y))
                count+=1
                for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if (i,j) in seen and union((i,j),(x,y)):
                        count-=1
            res.append(count)
        return res