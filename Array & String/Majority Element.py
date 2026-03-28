class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
                if freq[nums[i]]>n//2:
                    return nums[i]
                    break
            else:
                freq[nums[i]]=1

        return nums[i]
        
