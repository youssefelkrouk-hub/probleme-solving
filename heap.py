# -----------------------------
# Implémentation d’un Max-Heap
# -----------------------------

# Fonction pour obtenir l’indice de l’enfant gauche
def left(i):
    return 2 * i

# Fonction pour obtenir l’indice de l’enfant droit
def right(i):
    return 2 * i + 1

# Fonction pour obtenir l’indice du parent
def parent(i):
    return i // 2


# Maintient la propriété du max-heap à partir d’un nœud i
def max_heapify(a, heap_size, i):
    l = left(i)   # indice enfant gauche
    r = right(i)  # indice enfant droit

    largest = i   # supposons que le parent est le plus grand

    # comparer avec l’enfant gauche
    if l < heap_size and a[l] > a[i]:
        largest = l

    # comparer avec l’enfant droit
    if r < heap_size and a[r] > a[largest]:
        largest = r

    # si un enfant est plus grand que le parent
    if largest != i:
        # échanger parent et enfant
        a[i], a[largest] = a[largest], a[i]
        # appel récursif pour corriger plus bas
        max_heapify(a, heap_size, largest)


# Construit un max-heap à partir d’un tableau
def build_max_heap(a):
    heap_size = len(a)
    # on commence à heap_size//2 car les feuilles n’ont pas besoin d’être corrigées
    for i in range(heap_size // 2, 0, -1):
        max_heapify(a, heap_size, i)


# Retourne l’élément maximum (racine du tas)
def heap_maximum(a):
    return a[1]


# Extrait et supprime le maximum du tas
def heap_extract_max(a, heap_size):
    if heap_size < 1:
        raise Exception("Heap underflow")
    max_val = a[1]                # valeur max (racine)
    a[1] = a[heap_size - 1]       # déplacer le dernier élément à la racine
    heap_size -= 1
    max_heapify(a, heap_size, 1)  # restaurer la propriété du tas
    return max_val, heap_size


# Augmente la valeur d’un nœud et le remonte si nécessaire
def heap_increase_key(a, i, key):
    if key < a[i]:
        raise Exception("Nouvelle clé plus petite que l’ancienne")
    a[i] = key
    # remonter tant que le parent est plus petit
    while i > 1 and a[parent(i)] < a[i]:
        a[i], a[parent(i)] = a[parent(i)], a[i]
        i = parent(i)


# Insère une nouvelle clé dans le tas
def max_heap_insert(a, key, heap_size):
    heap_size += 1
    if heap_size >= len(a):
        a.append(float('-inf'))  # ajouter une case vide
    else:
        a[heap_size] = float('-inf')
    # augmenter la clé pour la placer correctement
    heap_increase_key(a, heap_size, key)
    return heap_size


# -----------------------------
# Exemple d’utilisation
# -----------------------------
def main():
    # Tableau avec None à l’indice 0 (pour simplifier les calculs)
    a = [None, 0, 5, 20, 6, 12, 65, 1, 4, 9, 3, 89, 22, 25, 28, 10]

    # Construire le max-heap
    build_max_heap(a)
    heap_size = len(a)

    print("Heap construit:", a[1:])
    print("Maximum:", heap_maximum(a))

    # Extraire le maximum
    max_val, heap_size = heap_extract_max(a, heap_size)
    print("Après extract max:", a[1:heap_size], "max extrait =", max_val)

    # Insérer une nouvelle clé
    heap_size = max_heap_insert(a, 100, heap_size)
    print("Après insertion de 100:", a[1:heap_size])


main()
