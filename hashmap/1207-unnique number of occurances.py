from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for num in arr:
            if num in freq :
                freq[num] += 1
            else :
                freq[num] = 1

        occurrences = list(freq.values())

        return len(occurrences) == len(set(occurrences))