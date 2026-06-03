from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k_tuples = Counter(nums).most_common(k)
        return [num for num, count in top_k_tuples]
