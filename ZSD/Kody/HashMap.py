
# Tworzenie słownika (HashMap)
d = {"name": "Jan", "surname": "Kowalski", "age": 20}

# Odczyt wartości
print(d["name"])                        # Jan

# Dodawanie nowej pary
d["city"] = "Cracow"

# Aktualizacja wartości
d["age"] = 21

# Sprawdzanie, czy klucz istnieje
if "name" in d:                         # Key exists
    print("Key exists")
else:
    print("Key does not exist")

if "phone_number" in d:                 # Key does not exist
    print("Key exists")
else:
    print("Key does not exist")

# Usuwanie elementu
del d["city"]

# Iteracja po kluczach i wartościach    # name -> Jan
for key, value in d.items():            # surname -> Kowalski
    print(key, "->", value)             # age -> 21

# Liczba elementów
print(len(d))                            # 3   

