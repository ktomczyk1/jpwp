
import heapq
from numpy import size

heap = [
    2,
    5, 3,
    11, 7, 6, 4,
    14, 12, 10, 9, 13, 16, 8
]

heapq.heapify(heap)

print("Initial heap: ", heap)
# [2, 5, 3, 11, 7, 6, 4, 14, 12, 10, 9, 13, 16, 8]

print(size(heap))       # 14

# Wstawianie elementu
heapq.heappush(heap, 1)
print("New heap: ", heap)
# [1, 5, 2, 11, 7, 6, 3, 14, 12, 10, 9, 13, 16, 8, 4]

# Usuwanie najmniejszego elementu
min_value = heapq.heappop(heap)
print("Removed value: ", min_value)         # 1
print("New heap: ", heap)
# [2, 5, 3, 11, 7, 6, 4, 14, 12, 10, 9, 13, 16, 8]


# Zamiana minimum na nowy element (heapreplace)
result = heapq.heapreplace(heap, 20)
print("Replaced element: ", result)        # 2
print("New heap: ", heap)       
# [3, 5, 4, 11, 7, 6, 8, 14, 12, 10, 9, 13, 16, 20]

# Optymalne push + pop (heappushpop)
result = heapq.heappushpop(heap, 5)
print("Returned element: ", result)        # 3
print("New heap: ", heap)
# [4, 5, 5, 11, 7, 6, 8, 14, 12, 10, 9, 13, 16, 20]

# n najmniejszych elementów
smallest = heapq.nsmallest(3, heap)
print("3 smallest elements: ", smallest)
# [4, 5, 5]

# n największych elementów
largest = heapq.nlargest(3, heap)
print("3 largest elements:", largest)
# [20, 16, 14]

