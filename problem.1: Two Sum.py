"""Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to 'target'.
We may assume that each input would have exactly one solution, and you may not use the same element twice."""

def twoSum(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
print(twoSum([2,7,11,6],9))   #  [0,1]; 2 + 7 = 9
# other test cases:
# [3,3],6 -> [0,1]
# [2,5],10 -> [0,1]
