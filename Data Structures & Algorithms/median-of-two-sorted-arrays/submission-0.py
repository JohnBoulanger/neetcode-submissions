class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        # store smaller array in A 
        if len(A) > len(B):
            A, B = B, A

        half = (len(A) + len(B) + 1) // 2

        # if we take i items from A, we need to take half - i items from B 
        # so that we have half of the items left of i and j between A and B
        # and half of them to the right
        l, r = 0, len(A)
        while True:
            i = (l + r) // 2
            j = half - i
            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < len(A) else float('inf')
            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < len(B) else float('inf')

            # found correct cut
            if Aleft <= Bright and Bleft <= Aright:
                if (len(A) + len(B)) % 2 == 0:
                    return ((Aleft if Aleft >= Bleft else Bleft) + (Aright if Aright <= Bright else Bright)) / 2
                else:
                    return max(Aleft, Bleft)
            # took too many in A, shrink it
            elif Aleft > Bright:
                r = i - 1
            # didnt take enough for A, grow it
            else:
                l = i + 1

        return -1
