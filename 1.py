class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lft=0
        rft=0
        for i in range(0,len(nums)):
            lft=i
            r=target-nums[i]
            for j in range(i+1,len(nums)):
                if(nums[j]==r):
                    rft=j
            if rft!=0:
              return [lft,rft]
            
