from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        # list of length n full of empty list
        bucket = [[] for _ in range(len(nums) + 1)]

        # numbers with largest frequency appear at the end of the bucket
        for key in freq_map:
            bucket[freq_map[key]].append(key)

        # iterate over bucket backwards and add k results
        result = []
        for i in range(len(bucket) - 1, -1, -1):
            for val in bucket[i]:
                result.append(val)
                if len(result) == k:
                    return result