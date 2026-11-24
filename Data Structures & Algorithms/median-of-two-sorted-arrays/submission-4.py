class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # a holds smaller array
        if len(A) > len(B):
            A, B = B, A

        # half of the values should be in the left half of A and B combined (or one more hence + 1)
        half = (len(A) + len(B) + 1) // 2
        l, r = 0, len(A)
        while True:
            # calculate midpoint of A
            i = (l + r) // 2
            # take whatever we need from B so items left of A + items left of B = half (half = half - i + i)
            j = half - i
            # get numbers left of split and right of split if OOB --> +/- inf
            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            # crossovers are correct, return median
            if Aleft <= Bright and Bleft <= Aright:
                if (len(A) + len(B)) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    # left because of + 1
                    return max(Aleft, Bleft)

            # took too many in A, take smaller amount
            elif Aleft > Bright:
                r = i - 1
            # didnt take enough in A, take more
            else:
                l = i + 1