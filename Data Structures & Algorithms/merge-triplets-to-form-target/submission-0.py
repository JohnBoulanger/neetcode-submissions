class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0, 0, 0]
        ta, tb, tc = target
        for i in range(len(triplets)):
            a, b, c = triplets[i]
            # update triplets if one of a b or c is better and all 3 are less than or equal the target triplet
            if a <= ta and b <= tb and c <= tc:
                cur[0] = max(a, cur[0])
                cur[1] = max(b, cur[1])
                cur[2] = max(c, cur[2])

        return cur == target            
        