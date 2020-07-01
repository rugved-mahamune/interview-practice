class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        occured = set()
        final = set()
        nums.sort()
        for i in range(len(nums)-1):
            if(i==0 or (i > 0 and nums[i] != nums[i-1])):
                low = i+1
                high = len(nums)-1     
                target = 0 - nums[i]
                while(high>low):
                    if(nums[low] + nums[high] == target):
                        final.add((nums[i], nums[low], nums[high]))
                        while(low<high and nums[low]==nums[low+1]):
                            low+=1
                        while(low<high and nums[high]==nums[high-1]):
                            high-=1
                        low+=1
                        high-=1
                    elif(nums[low]+nums[high] < target):
                        low+=1
                    else:
                        high-=1
        return list(final)