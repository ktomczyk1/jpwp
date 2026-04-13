
queue = []

queue.append("Ala")
queue.append("Bartek")
queue.append("Celina")

print("Kolejka po dodaniu osób:", queue)

first_person = queue.pop(0)
print("Obsłużono osobę:", first_person)
print("Kolejka po usunięciu:", queue)

#Zrefaktoryzuj powyższy kod, tworząc funkcję 'enqueue(queue, value)',
#która dodaje element na koniec kolejki.
#Następnie utwórz funkcję 'dequeue(queue)', która usuwa i zwraca pierwszy element kolejki.
#Użyj tych funkcji zamiast append() i pop(0).
#Na samym końcu wypisz stan kolejki.