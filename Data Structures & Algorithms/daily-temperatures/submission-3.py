class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i in range(n):
            if not stack:
                stack.append((temperatures[i], i)) # (value, index)
            else:
                if (stack[-1][0] >= temperatures[i]):
                    stack.append((temperatures[i], i))
                else:
                    while(stack and stack[-1][0] < temperatures[i]):
                        _ , index = stack.pop()
                        res[index] = i - index
                    stack.append((temperatures[i], i))
        while (stack):
            res[stack[-1][1]] = 0
            stack.pop()
        return res
