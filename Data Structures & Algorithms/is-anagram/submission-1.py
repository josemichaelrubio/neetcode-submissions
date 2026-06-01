class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First check if length is the same for easy bool
        if len(s) != len(t):
            return False
        # Then, use Counter
        return Counter(s) == Counter(t)
        