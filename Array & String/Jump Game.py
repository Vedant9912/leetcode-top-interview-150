class Solution:
    def jump(self, nums: List[int]) -> int:
        maxranged=0
        jumps=0
        for i in range(len(nums)):
            if maxranged>=len(nums)-1:
                return jumps

            if maxranged<nums[i]+i:
                maxranged=nums[i]+i
                jumps+=1
