class Solution:
    def isPalindrome(self, x: str) -> bool:
        x = str(x)
        if x[0] == "-":
            return False
        x_invert = x[::-1]
        if x == x_invert:
            return True
        else:
            return False
        
print(Solution().isPalindrome(-121))