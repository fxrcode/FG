# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        n,groupA,groupB,aIdx,bIdx=reader.length(),1,0,None,None
        first,second=reader.query(0,1,2,3),reader.query(0,1,2,4)
        for i in range(4,n):
            if reader.query(0,1,2,i)==first:
                groupA,aIdx=groupA+1,i
            else:
                groupB,bIdx=groupB+1,i
        for i in range(3):
            nxt=[v for v in [0,1,2,3,4] if v!=i]
            if reader.query(*nxt)==second:
                groupA,aIdx=groupA+1,i
            else:
                groupB,bIdx=groupB+1,i
        return aIdx if groupA>groupB else bIdx if groupB>groupA else -1