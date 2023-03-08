class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        invert_index = defaultdict(list)
        for prev, ch in enumerate(source):
            invert_index[ch].append(prev)

        # Initialize prev = -1 (i represents the smallest valid next offset)
        # loop_cnt = 1 (number of passes through source). My pov: this means we need to start a new subseq
        loop_cnt = 1
        prev = -1
        for ch in target:
            if ch not in invert_index:
                return -1
            offset_list_for_ch = invert_index[ch]
            j = bisect_right(offset_list_for_ch, prev)
            if j == len(offset_list_for_ch):
                loop_cnt += 1
                prev = offset_list_for_ch[0]
            else:
                prev = offset_list_for_ch[j]
        return loop_cnt