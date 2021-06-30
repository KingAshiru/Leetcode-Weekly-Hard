from heapq import *
from collections import deque
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        char_freq = {}
        for char in s:
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1
        
        max_heap = []
        for key, val in char_freq.items():
            heappush(max_heap, (-val, key))
        
        res = []
        queue = deque()
        
        while max_heap:
            freq, char = heappop(max_heap)
            res.append(char)
            queue.append((char, freq + 1))
            if len(queue) >= k:
                cha, frq = queue.popleft()
                if -frq > 0:
                    heappush(max_heap, (frq, cha))
            
        return "".join(res) if len(res) == len(s) else ""
                
