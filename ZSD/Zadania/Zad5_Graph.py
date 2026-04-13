
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

print("Sąsiedzi wierzchołka A:", graph["A"])
print("Sąsiedzi wierzchołka B:", graph["B"])

#Zrefaktoryzuj powyższy kod, tworząc funkcję 'bfs(graph, start)',
#która przeszukuje graf wszerz od podanego wierzchołka startowego.
#Użyj kolejki do odwiedzania kolejnych wierzchołków.
#Dodatkowo utwórz funkcję 'dfs(graph, start)',
#która przeszukuje graf w głąb od tego samego wierzchołka startowego.
#Użyj stosu lub rekurencji.
#Na końcu wypisz kolejność odwiedzania wierzchołków dla BFS i DFS, zaczynając od "A".


# PODPOWIEDZ: PREZENTACJA