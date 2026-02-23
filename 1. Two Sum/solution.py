from typing import List
def two_sum(n: List[int], m: int) ->List[int]:
    """
    Finds two indices in the list 'n' such that their values sum to 'm'.
    Returns the indices as a list [i, j].
    """
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[i] + n[j] == m:
                return [i, j]
            
print(two_sum([2, 7, 11, 15], 9))   # Output: [0, 1]
