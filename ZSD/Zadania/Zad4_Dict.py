
phone_book = {
    "Ania": "123-456-789",
    "Bartek": "987-654-321",
    "Celina": "555-111-222"
}

numbers_set = {2, 4, 6, 8, 10}

print("Numer Ani:", phone_book["Ania"])
print("Czy 6 jest w zbiorze?", 6 in numbers_set)
print("Czy 7 jest w zbiorze?", 7 in numbers_set)

#Zrefaktoryzuj powyższy kod, tworząc funkcję 'find_number(phone_book, name)',
#która zwraca numer telefonu podanej osoby ze słownika.
#Następnie utwórz funkcję 'check_in_set(numbers_set, value)',
#która sprawdza, czy podana wartość znajduje się w zbiorze.
#Użyj tych funkcji zamiast bezpośredniego odwołania do słownika i operatora 'in'.
#Na końcu wypisz wyniki dla imienia 'Ania' oraz wartości 6 i 7.