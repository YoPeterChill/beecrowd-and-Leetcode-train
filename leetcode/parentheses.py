class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        stack = []
        start = 0
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append(c)
            else:
                stack.pop()
                
                if not stack:
                    result += s[start + 1:i]
                    start = i + 1
                    
        return result

# Predefine the string s
s = "(()())(())(()(())"

# Create an instance of Solution and call the method
solution = Solution()
output = solution.removeOuterParentheses(s)
print(output)  # Expected output: "()()()()(())"