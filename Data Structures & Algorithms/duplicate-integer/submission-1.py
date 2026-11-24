class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq_items = set()

        for num in nums:
            if num in uniq_items:
                return True
            else:
                uniq_items.add(num)

        return False