# 2149. Rearrange Array Elements by Sign
class Solution(object):
    def rearrangeArray(self, nums):
        nump=[]
        numn=[]
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                nump.append(nums[i])
            else:
                numn.append(nums[i])
        for j in range(len(nums)/2):
            res.append(nump[j])
            res.append(numn[j])
        return res
