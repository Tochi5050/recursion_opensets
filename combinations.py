from collections import deque


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        comb = []
        queue = deque()

        for idx in range(1, n + 1):
            queue.append((idx, idx))

            if k == 1:
                result.append([idx])

        while queue:
            *val, index = queue.popleft()

            for idx in range(index, n):
                if idx < n:
                    comb.extend([*val, (idx + 1)])
                    # print(comb)
                    if len(comb) == k:
                        result.append(comb)
                        comb = []
                        continue
                    else:
                        tuple_val = tuple(comb) + (idx + 1,)
                        queue.append(tuple_val)
                        comb = []
        return result


