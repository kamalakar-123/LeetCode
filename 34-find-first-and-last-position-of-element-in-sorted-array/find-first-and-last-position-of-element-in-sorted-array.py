class Solution:
    def binarySearchLeft(self, nums, target):
        n          = len(nums)
        low, high  = 0, n - 1
        index      = -1              

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid          
                high  = mid - 1      
            elif nums[mid] > target:
                high  = mid - 1      
            else:                   
                low   = mid + 1      
        return index

   
    def binarySearchRight(self, nums, target):
        n          = len(nums)
        low, high  = 0, n - 1
        index      = -1              

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid          
                low   = mid + 1      
            elif nums[mid] > target:
                high  = mid - 1
            else:                    #
                low   = mid + 1
        return index
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        ext_left = self.binarySearchLeft(nums, target)
        
        if ext_left == -1:
            return [-1, -1]

        ext_right = self.binarySearchRight(nums, target)
        return [ext_left, ext_right]
        