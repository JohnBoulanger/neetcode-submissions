class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # store the smaller array in A
        if len(A) > len(B):
            A, B = B, A

        half = (len(A) + len(B) + 1) // 2

        # find the point where you can split A and B so half the numbers combined are at a split point
        # left of A and B (different splits) and right of A and B (diff splits) where their crossovers are
        # correctly increasing

        l, r = 0, len(A)

        while True:
            # split point for A
            i = (l + r) // 2
            # split point for B so there are equally many numbers left of A and B combined as there are right
            j = half - i

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if (len(A) + len(B)) % 2 == 0:
                    return ((Aleft if Aleft >= Bleft else Bleft) + (Aright if Aright <= Bright else Bright)) / 2
                else:
                    return max(Aleft, Bleft)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

        return -1




        