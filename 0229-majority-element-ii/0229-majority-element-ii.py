class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n,count=len(nums),[]
        num=set(nums)
        for i in num:
            if nums.count(i)>n/3:
                count.append(i)
        return count