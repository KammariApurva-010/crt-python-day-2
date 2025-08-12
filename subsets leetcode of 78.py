class Solution:
    def subsets(self,nums):
        n=len(nums)
        total_subsets=(1<<n)
        ans=[]
        for num in range(total_subsets):
            temp=[]
            for i in range(n): #n=3
                if((num&(1<<i))!=0):
                    temp.append(nums[i])
            ans.append(temp)
        return ans
nums=list(map(int,input().split())) 
ob=Solution()
print(ob.subsets(nums))