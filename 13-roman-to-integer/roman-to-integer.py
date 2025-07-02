class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        maps = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range (1, len(s)):
            if maps[s[i]] > maps[s[i-1]]:
                ans = ans - maps[s[i-1]]
            else:
                ans = ans + maps[s[i-1]]
        ans = ans + maps[s[len(s)-1]]
        return ans


            