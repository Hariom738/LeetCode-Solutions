class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unq = []
        for i in nums:
            if nums.count(i)==1:
                unq.append(i)
        return sum(unq)
                
            
        