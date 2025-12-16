
# Données:
# - keys[] = [k₁, k₂, ..., kₙ] triées (ex: [10, 20, 30, 40])
# - freq[] = [p₁, p₂, ..., pₙ] où pᵢ = probabilité de chercher kᵢ
# - Contrainte: Σ pᵢ = 1

# Objectif:
# Construire un arbre binaire de recherche qui MINIMISE:
# Coût_attendu = Σ (profondeur(kᵢ) × pᵢ)

# Où profondeur(kᵢ) = nombre de comparaisons nécessaires pour trouver kᵢ
# (racine = profondeur 1)

print("la methode naive consiste a generer tous les arbres binaire possibles puis calculer leurs cost et enfin choisir celle qui min(costs)")
# c'est trés couteux en terme de temps 
# ! Nombre de BST avec n clés = Nombre de Catalan Cₙ
# Cₙ = (1/(n+1)) × (2n choose n) ≈ 4ⁿ / (n^(3/2) × √π)

# la solution est donc d'utiliser DP = Memoisation+recursion 


def obst_dp(keys, freq):
    n = len(keys)
    cost = [[0] * n for _ in range(n)]

    for length in range(1, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            cost[i][j] = float('inf')
            
            for r in range(i, j+1):
                left = cost[i][r-1] if r > i else 0
                right = cost[r+1][j] if r < j else 0
                total = left + right + sum(freq[i:j+1])
                
                if total < cost[i][j]:
                    cost[i][j] = total
    
    return cost[0][n-1]

# -------------------------------------------------
# TEST 1: Données de base
# -------------------------------------------------
print("="*60)
print("TEST 1: 4 clés avec fréquences variées")
print("="*60)

keys1 = ["A", "B", "C", "D"]
freq1 = [0.1, 0.2, 0.3, 0.4]  # Total = 1.0

result1 = obst_dp(keys1, freq1)
print(f"Clés: {keys1}")
print(f"Fréquences: {freq1}")
print(f"Coût optimal: {result1:.3f}")

# Vérification manuelle
print("\nVérification manuelle:")
print("Le coût devrait être environ 1.9 pour cet exemple.")
print("Calcul: F[0,3] + min des combinaisons = 1.0 + 0.9 = 1.9")
