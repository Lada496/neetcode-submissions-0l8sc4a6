# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs) - 1)
    
    def quickSortHelper(self, pairs, s, e) -> List[Pair]:
        
        if e - s <= 0:
            return pairs

        pivot = pairs[e]

        smaller = s
        i = s
        while i <= e:
            if pairs[i].key < pivot.key:
                tmp = pairs[smaller]
                pairs[smaller] = pairs[i]
                pairs[i] = tmp
                smaller += 1
            i += 1
        #left = pairs[: smaller]
        #right = pairs[smaller + 1:]

        tmp = pairs[smaller]
        pairs[smaller] = pivot
        pairs[e] = tmp

        self.quickSortHelper(pairs, s, smaller - 1)
        self.quickSortHelper(pairs, smaller + 1, e)

        return pairs
            

        