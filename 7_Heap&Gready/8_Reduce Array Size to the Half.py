"""Reduce Array Size to the Half."""

from collections import Counter
import heapq
import sys


def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    arr = data[1 : n + 1]

    freq = Counter(arr)
    max_heap = [-count for count in freq.values()]
    heapq.heapify(max_heap)

    removed = 0
    chosen = 0
    target = n // 2

    while removed < target:
        removed += -heapq.heappop(max_heap)
        chosen += 1

    print(chosen)


if __name__ == "__main__":
    solve()
