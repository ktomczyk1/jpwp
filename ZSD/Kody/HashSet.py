
# Tworzenie zbioru (HashSet)
s = {"apple", "banana", "orange"}

# Odczyt / sprawdzanie elementu (czy istnieje)
print("apple" in s)                 # True
print("strawberry" in s)            # False

# Dodawanie elementu
s.add("pear")

# Dodanie istniejącego elementu (nic się nie zmienia)
s.add("apple")

# Usuwanie elementu
s.remove("banana")

# Iteracja po elementach            # apple
for item in s:                      # orange
    print(item)                     # pear

# Liczba elementów
print(len(s))                       # 3

# Automatyczne prawdzanie unikalności, duplikaty są ignorowane
s.add("orange")
print(s)                            # {'apple', 'orange', 'pear'}

# Usuwanie elementu (wyrzuci błąd)
s.remove("pineapple")

# Bezpieczne usuwanie (nie wyrzuci błędu, jeśli nie ma elementu)
s.discard("pineapple")