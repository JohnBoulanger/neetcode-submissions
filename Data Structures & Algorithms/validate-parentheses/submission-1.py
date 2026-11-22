class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            # add the character to the top of the stack
            stack.append(ch)
            # if its a closing bracket
            if ch == "]" or ch == "}" or ch == ")":
                # remove a matching pair if it exists
                while stack and stack[-2:] == ["[", "]"] or stack[-2:] == ["{", "}"] or stack[-2:] == ["(", ")"]:
                    stack.pop()
                    stack.pop()

        return len(stack) == 0