print("Mergin Two Sorted Arrays with TOW POINTER TECHNIQUE")
def mergeArrays(arr1, arr2):
    merged=[ ]
    i,j=0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merged.append(arr1[i])
            i=i+1
        else:
            merged.append(arr2[j])
            j=j+1
    merged.extend(arr1[i:]) # ajouter les elements restants de arr1 dés que la boucle while est terminée
    merged.extend(arr2[j:]) # ajouter les elements restants de arr2
    return merged
 
print(mergeArrays([1,3,5],[2,4,6,8,10])) # [1,2,3,4,5,6,8,10]


print("appication de Optiomal Merge Pattern in Huffman Coding")
import heapq
def optimalMergePattern(file_sizes):
    heapq.heapify(file_sizes)  # Convertir la liste en un tas min-heap
    total_cost = 0
    while len(file_sizes) > 1:
        # Extraire les deux plus petits fichiers
        first = heapq.heappop(file_sizes)
        second = heapq.heappop(file_sizes)
        # Coût de fusionner ces deux fichiers
        merge_cost = first + second
        total_cost += merge_cost
        # Insérer le fichier fusionné de nouveau dans le tas
        heapq.heappush(file_sizes, merge_cost)
    return total_cost

print(optimalMergePattern([4, 3, 2, 6]))  # Output: 29

print("Huffman Coding Implementation") 

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char        # caractère
        self.freq = freq        # fréquence
        self.left = None        # fils gauche
        self.right = None       # fils droit

    # Comparaison pour la min-heap
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_codes(chars, freqs):
    # Créer une min-heap avec les nœuds
    heap = [Node(chars[i], freqs[i]) for i in range(len(chars))]
    heapq.heapify(heap)

    # Construire l’arbre de Huffman
    while len(heap) > 1:
        # Extraire les deux plus petites fréquences
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Créer un nouveau nœud combiné
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Réinsérer dans la heap
        heapq.heappush(heap, merged)

    # Racine de l’arbre
    root = heap[0]

    # Générer les codes en parcourant l’arbre
    codes = {}
    def generate_codes(node, current_code=""):
        if node is None:
            return
        if node.char is not None:  # feuille
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root)
    return codes

# Exemple d’utilisation
chars = ['A', 'B', 'C', 'D', 'E']
freqs = [3, 5, 6, 4, 2]

codes = huffman_codes(chars, freqs)
print("Codes de Huffman :")
for char in codes:
    print(f"{char}: {codes[char]}")
