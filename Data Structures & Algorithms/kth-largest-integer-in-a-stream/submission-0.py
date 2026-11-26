class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # create a heap from the stream holding the k largest elements
        self.h = []
        self.k = k
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        # only hold k elemens will be k largest
        if len(self.h) > self.k:
            heapq.heappop(self.h)

        return self.h[0]
