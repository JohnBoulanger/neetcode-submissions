from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create buckets where the index maps to the number of times
        # a number appeared in that list of length len(nums) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # create a frequency map
        counter = Counter(nums)

        # fill buckets
        for key, val in counter.items():
            buckets[val].append(key)

        result = []
        # go through all buckets backwards
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            # add the top k numbers from the buckets
            for item in bucket:
                result.append(item)
                if len(result) == k:
                    return result