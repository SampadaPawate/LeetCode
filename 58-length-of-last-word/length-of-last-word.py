class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])



        # count=0
        # txt=s.strip()
        # txt=txt[::-1]
        # for i in txt:
        #     if i==" ":
        #         break
        #     else:
        #         count+=1
                
            
        # return count







        # s=s.strip()
        # count=0
        # for i in s:
        #     if i==" " :
        #         count=0

        #     else:
        #         count+=1
        # return count
        