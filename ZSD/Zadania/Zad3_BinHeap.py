
import heapq

tasks = []

heapq.heappush(tasks, 3)
heapq.heappush(tasks, 1)
heapq.heappush(tasks, 2)

print("Kolejka priorytetowa:", tasks)

highest_priority = heapq.heappop(tasks)
print("Usunięty element o najwyższym priorytecie:", highest_priority)
print("Stan kolejki po usunięciu:", tasks)

#Zrefaktoryzuj powyższy kod, tworząc funkcję 'add_task(tasks, priority)',
#która dodaje element do kolejki priorytetowej za pomocą heapq.heappush().
#Następnie utwórz funkcję 'get_task(tasks)', która usuwa i zwraca element
#o najniższym priorytecie (najmniejszej wartości) za pomocą heapq.heappop().
#Użyj tych funkcji zamiast bezpośrednich wywołań heapq.heappush() i heapq.heappop().
#Na końcu wypisz aktualny stan kolejki priorytetowej.