class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"}": "{", "]": "[", ")": "("}
        for ch in s:
            # if its a closing bracket
            if ch in match:
                # remove a matching pair if it exists
                if stack and match[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            # add right bracket to stack
            else:
                stack.append(ch)
            

        return len(stack) == 0