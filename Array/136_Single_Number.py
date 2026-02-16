class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ht={}
        for num in nums:
            if num in ht:
                ht[num]+=1
            else:
                ht[num]=1
        for num,count in ht.items():
            if count%2!=0 :
                return num
