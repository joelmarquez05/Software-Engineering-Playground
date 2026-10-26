class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        expected = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in expected:
                stack.append(expected[char]) 
            else:
                if not stack:
                    return False
                if char != stack[-1]:
                    return False
                stack.pop()

        return not stack