
class Solution:
    def checkValidString(self, s: str) -> bool:
        lp = []
        star = []

        for i, c in enumerate(s):
            if c == "(": lp.append(i)
            if c == "*": star.append(i)
            # check if we have ( or * for a )
            if c == ")":
                if lp:
                    lp.pop()
                elif star:
                    star.pop()
                else:
                    return False

        # remove all remaining ( 
        while lp:
            # only remove ( if it has a corresponding * in front of it
            if not star or lp[-1] > star[-1]:
                return False
            else:
                lp.pop()
                star.pop()

        return True

            