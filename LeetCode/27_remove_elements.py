class Solution:
    def removeElement(self, nums, val):
        tmp = None
        for i in range(0, len(nums) - 1):
            if nums[i] == val:
                tmp = nums[i + 1]
                nums[i + 1] = nums[i]
                nums[i] = '_'
            else:
                pass
    

        

s = Solution()

nums = [3,2,2,3,3,3,2,4,2,3,4]
val = 3

s.removeElement(nums, val)
print(nums)
