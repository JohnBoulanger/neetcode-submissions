class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], ""

        def backtrack(s, opens, closes):
            # solution found
            if len(s) == 2 * n:
                res.append(s)
                return
            # case to add an open parenthesis
            if opens < n and closes < n:
                backtrack(s + "(", opens + 1, closes)
            # case to add a closed parenthesis
            if opens > closes and closes < n:
                backtrack(s + ")", opens, closes + 1)

        backtrack("", 0, 0)
        return res