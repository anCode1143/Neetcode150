from collections import defaultdict
from typing import List
import heapq

def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    hand.sort()
    numberCount = defaultdict(int)
    for card in hand:
        numberCount[card] += 1
    heap = list(numberCount.keys())
    heapq.heapify(heap)
    while heap:
        if numberCount[heap[0]] == 0:
            heapq.heappop(heap)
            continue
        start = heap[0]
        for cardIndex in range(groupSize):
            if numberCount[start + cardIndex] == 0:
                return False
            numberCount[start + cardIndex] -= 1
    return True