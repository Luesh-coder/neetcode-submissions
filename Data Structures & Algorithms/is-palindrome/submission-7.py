class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        use two pointers

        left and right pointers

        while left index is less than rigth index:
            while left index < right index and isn't alphanumeric:
                left += 1
            while right index > left index and isn't alphanumeric:
                right -= 1
            if character[l] != character[r]:
                return false
            l, r = l + 1, r - 1
        return True if it iterates through loop

        """
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
            
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9') or
                ord('a') <= ord(c) <= ord('z'))
        
