class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(path, opens, closes):
            if len(path) == 2*n:
                result.append(path)
                return
            if opens < n:
                backtrack(path + "(", opens + 1, closes)
            if opens > closes:
                backtrack(path + ")", opens, closes + 1)
            return

        backtrack("", 0, 0)
        return result
