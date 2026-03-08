# Last updated: 3/8/2026, 3:16:20 PM
class Solution(object):
    def productExceptSelf(self, nums):
        res=[]
        k=1
        for m in range(len(nums)):
            k*=nums[m]
        


        for i in range(len(nums)):
            s=1
            if nums[i]==0:
                for n in range(len(nums)):
                    

                    if n!=i:
                        s*=nums[n]
                res.append(s)


            else:
                res.append(k/nums[i])
            
        return res

        
        