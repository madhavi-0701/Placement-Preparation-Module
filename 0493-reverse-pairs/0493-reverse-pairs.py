class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count=0
        if len(nums)>1:
            mid=len(nums)//2
            left=nums[:mid]
            right=nums[mid:]
            count+=self.reversePairs(left)
            count+=self.reversePairs(right)
            i=0
            j=0
            for i in range(len(left)):
                while j<len(right) and left[i]>right[j]*2:
                    j+=1
                count+=j
            i=j=k=0        
            while i<len(left) and j<len(right):
                if left[i]>right[j]:
                    nums[k]=right[j]
                    j+=1
                    k+=1
                else:
                    nums[k]=left[i]
                    i+=1
                    k+=1
            while j<len(right):
                nums[k]=right[j]
                j,k=j+1,k+1
            while i<len(left):
                nums[k]=left[i]
                i,k=i+1,k+1     
        return count