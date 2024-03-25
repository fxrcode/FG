class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        from sortedcontainers import SortedDict

        sd = SortedDict()
        for s,e in intervals:
          sd[s] = sd.setdefault(s, 0) + 1
          sd[e] = sd.setdefault(e,0)-1
        room, k = 0,0
        for _,v in sd.items():
          room += v
          k = max(k, room)
        return k