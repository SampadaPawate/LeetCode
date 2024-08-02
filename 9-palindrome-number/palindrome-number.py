class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans=str(x)
        if ans==ans[::-1]:
            return True
        else:
            return False
