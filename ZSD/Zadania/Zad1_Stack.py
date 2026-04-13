
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stos po dodaniu elementów:", stack)

last_element = stack.pop()
print("Usunięty element:", last_element)
print("Stos po usunięciu:", stack)

#Zrefaktoryzuj powyższy kod, tworząc funkcję 'push_element(stack, value)',
#która dodaje element na stos.
#Następnie utwórz funkcję 'pop_element(stack)', która usuwa i zwraca ostatni element.
#Użyj tych funkcji zamiast bezpośredniego wywoływania append() i pop().
#Na samym końcu wypisz stan stosu.