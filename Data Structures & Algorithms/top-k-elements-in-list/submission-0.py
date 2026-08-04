from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counts = Counter(nums)
        top = nums_counts.most_common(k)
        return [item[0] for item in top]
