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
print("Buttom up approach")

def min_coins_dp(coins, amount):
    # Initialiser le tableau pour stocker le nombre minimum de pièces pour chaque montant
    dp = [0] * (amount + 1)
    dp[0]=0  # 0 pièces sont nécessaires pour faire le montant 0
    for i in range(1,amount+1):
        dp[i]=float('inf')
        for coin in coins:
            if i-coin>=0:
                dp[i]=min(dp[i],dp[i-coin]+1)
    return dp[amount]

# Exemple d'utilisation
print(min_coins_dp([1, 5, 10, 25], 63))  # Output: 6 (2x25 + 1x10 + 3x1)
print(min_coins_dp([1, 4, 5], -13))  # Output: 3  (2x4 + 1x5)
print("Top Down Approach with Memoization")
#Memoization is storing the results of expensive function calls and reusing them when the same inputs occur again.
memo={}
def min_coins_td(coins,amount):
    if amount==0:
        return 0
    if amount in memo:
        return memo[amount]
    min_coins=float('inf') #pour chaque montant, initialiser le nombre minimum de pièces à l'infini
    for coin in coins:
        if amount-coin>=0:
            num_coins=min_coins_td(coins,amount-coin) 
            min_coins=min(min_coins,num_coins+1) 
    memo[amount]=min_coins
    return memo[amount]

print(min_coins_td([1, 4, 5], 13))  # Output: 3  (2x4 + 1x5)
        
