
import heapq
from numpy import size

heap = [
    -9,
    -8, -6,
    -7, -2, -3, -4,
    -1 , -5
]

heapq.heapify(heap)

print("Initial heap: ", heap)
# [-9, -8, -6, -7, -2, -3, -4, -1, -5]
# interpretujemy jako:
# [9, 8, 6, 7, 2, 3, 4, 1, 5]

# Wstawianie elementu
heapq.heappush(heap, -10)
print("New heap: ", heap)
# [-10, -9, -6, -7, -8, -3, -4, -1, -5, -2]
# interpretujemy jako:
# [10, 9, 6, 7, 8, 3, 4, 1, 5, 2]

