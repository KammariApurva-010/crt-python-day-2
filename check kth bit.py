class Solution:
    def checkKthBit(self,n,k):
        if((n&(1<<k))==0):
             return False
        return True
n=int(input())
k=int(input())
ob=Solution()
print(ob.checkKthBit(n,k))