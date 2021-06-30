from heapq import heappop, heappush
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0 or num < self.min_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        self.balance_heaps()

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            mid = (-self.max_heap[0] + self.min_heap[0]) / 2
            return mid
        return -self.max_heap[0]
    
    def balance_heaps(self):
        if len(self.max_heap) < len(self.min_heap):
            val = heappop(self.min_heap)
            heappush(self.max_heap, -val)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heappop(self.max_heap)
            heappush(self.min_heap, -val)
        
            
 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
