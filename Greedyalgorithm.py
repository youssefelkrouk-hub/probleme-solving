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



print("Minumum Coin Problem")


print("Battumin de pieces pour un montant donné en utilisant l'algorithme glouton")

def minumum_coins_gloutoune(coins, amount):
    coins.sort(reverse=True)  # Trier les pièces en ordre décroissant
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    if amount == 0:
        return count
    else:
        return -1  # Impossible de faire le montant avec les pièces données
# Exemple d'utilisation
print(minumum_coins_gloutoune([1, 5, 10, 25], 63))  # Output: 6 (2x25 + 1x10 + 3x1)
print(minumum_coins_gloutoune([1, 4, 5], 13)) 
#dans le dernier exemple, l'algorithme glouton ne donne pas la solution optimale car il utilise 2 pièces de 5 et 3 pièces de 1 (total 5 pièces)
#alors que la solution optimale est 3 pièces (2 pièces de 4 et 1 pièce de 5)

print("Minmum coin par programmation dynamique")
print("Buttom up approach ou Tabulation Approach")

def min_coins_dp(coins, amount):
    # Initialiser le tableau pour stocker le nombre minimum de pièces pour chaque montant
    dp = [0] * (amount + 1) # Initialiser avec une grande valeur pour représenter l'infini pour chaque montant
    dp[0]=0  # 0 pièces sont nécessaires pour faire le montant 0
    for i in range(1,amount+1):
        dp[i]=10**8  # Initialiser avec une grande valeur pour représenter l'infini
        for coin in coins: #pour chaque pièce
            if i-coin>=0: #si le montant courant moins la valeur de la pièce est non négatif
                dp[i]=min(dp[i],dp[i-coin]+1) #mettre à jour le nombre minimum de pièces pour le montant i
    return dp[amount] # retourner le nombre minimum de pièces pour le montant donné

# Exemple d'utilisation
print(min_coins_dp([1, 5, 10, 25], 63))  # Output: 6 (2x25 + 1x10 + 3x1)
print(min_coins_dp([1, 4, 5], 13))  # Output: 3  (2x4 + 1x5)
print("Top Down Approach with Memoization")
#Memoization is storing the results of expensive function calls and reusing them when the same inputs occur again.
memo={}
def min_coins_td(coins,amount):
    if amount==0:
        return 0
    if amount in memo:
        return memo[amount]
    min_coins=10**8 #pour chaque montant, initialiser le nombre minimum de pièces à l'infini 
    for coin in coins:
        if amount-coin>=0:
            num_coins=min_coins_td(coins,amount-coin) 
            min_coins=min(min_coins,num_coins+1) 
    memo[amount]=min_coins
    return memo[amount]

print(min_coins_td([1, 4, 5], 13))  # Output: 3  (2x4 + 1x5)
print(min_coins_dp([1, 5, 10, 25], 63))  # Output: 6 (2x25 + 1x10 + 3x1)
#Kruskal's Algorithm : trier les arêtes par poids croissant et ajouter les arêtes au MST en évitant les cycles jusqu'à ce que tous les sommets soient inclus.

print("Algorithm de Floyd-Warshall pour le plus court chemin entre toutes les paires de sommets dans un graphe pondéré:")
# cette algorithme utilise la programmation dynamique pour trouver les plus courts chemins entre tous les paires de sommets dans un graphe pondéré.
import numpy as np


def floyd_warshall(graph):
    # Initialiser la matrice des distances
    # dist = [[float('inf')] * len(graph) for _ in range(len(graph))]
    # for i in range(len(graph)):
    #     for j in range(len(graph)):
    #         if i == j:
    #             dist[i][j] = 0
    #         elif graph[i][j] != 0:
    #             dist[i][j] = graph[i][j]
    dist=graph.copy()
    # Mettre à jour les distances en utilisant chaque sommet comme intermédiaire
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                dist[i,j]=min(dist[i][j],dist[i][k]+dist[k][j])
                #if dist[i][j] > dist[i][k] + dist[k][j]:
                    #dist[i][j] = dist[i][k] + dist[k][j]
            
    return dist

#time complexity O(V^3) where V is the number of vertices in the graph
#space complexity O(V^2) for storing the distance matrix

# Exemple d'utilisation
graph = np.array([[0, 3, float('inf'), 7],
                  [8, 0, 2, float('inf')],
                  [5, float('inf'), 0, 1],
                  [2, float('inf'), float('inf'), 0]])
shortest_paths = floyd_warshall(graph)
print("Matrice des plus courts chemins entre toutes les paires de sommets :")
print(shortest_paths)
shortest_paths=np.array(
[[0, 3, 5, 6],
 [7, 0, 2, 3],
 [3, 6, 0, 1],
 [2, 5, 7, 0]]

)

# le plus court chemin de 0 à 2 est 5 (0->1->2)
# le plus court chemin de 3 à 2 est 7 (3->0->1->2)

print("Plus longues sous-séquences communes (LCS) entre deux chaînes de caractères en utilisant la programmation dynamique")
print("Solved by using recursion : ")

def lcs_recursive(X, Y, m, n):
    # Cas de base : si l'une des chaînes est vide
    if m == 0 or n == 0:
        return 0
    # Si les derniers caractères sont les mêmes, ils font partie de la LCS
    if X[m-1] == Y[n -1]:
        return 1 + lcs_recursive(X, Y, m-1 , n -1)
    else:
        # Sinon, prendre le maximum entre deux cas :
        # 1. Ignorer le dernier caractère de X
        # 2. Ignorer le dernier caractère de Y
        return max(lcs_recursive(X, Y, m, n - 1), lcs_recursive(X, Y, m - 1, n))
    
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs_recursive(X, Y, len(X), len(Y)))  # Output: 4 (GTAB)