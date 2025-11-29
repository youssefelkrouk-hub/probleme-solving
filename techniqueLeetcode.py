print("============Tow Pointer Technique ==============")
def plaindrome(s):
    gauche,droite=0,len(s)-1
    while gauche<droite:
        if s[gauche]!=s[droite]:
            return False
        else:
            gauche=gauche+1
            droite=droite-1
    return True
print("Version améliore pour une phrase")
def isPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        # Ignorer les caractères non alphanumériques
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        # Comparer en minuscule
        if s[left].lower() != s[right].lower():
            return False
        # Avancer les pointeurs
        left += 1
        right -= 1
    return True
# Exemple d'utilisation
print(isPalindrome("A man, a plan, a canal Panama"))  # True
print(isPalindrome("race a car"))                      # False

def pairs(L,target):
    left=0
    right=len(L)-1
    while left!=right:
        current_sum=L[left]+L[right]
        if current_sum==target:
            return L[left],L[right] ,left,right
        elif current_sum<target:
            left=left+1
        else:
            right=right-1
    return L[left],L[right]

def trois_number(L,target):
    n=len(L)
    for i in range(n-2):
        left=i+1 # aux moins  left prend la valeur suivante de i 
        right=n-1
        while left<right:
            current_sum=L[i]+L[left]+L[right]
            if current_sum==target:
                return L[i],L[left],L[right]
            elif current_sum<target:
                left=left+1
            else:
                right=right-1
        return L[i],L[left],L[right]


print(pairs([0,3,15,20],35))
print(trois_number([1,2,3,4,5,6,7,8,10],18))

print("=========Probleme Container With Most Water ==============")
def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        # Calculer l'aire actuelle
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        # Déplacer le pointeur de la hauteur minimale
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
print(maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49 # 1 et 8 qui forme le container le plus grand

print("======= Sliding Window technique =======")

#cette methode sert a trouver la somme maximale d'une sous-liste de taille k dans une liste donnée



# la premiere étape consiste à calculer la somme initiale des k premiers éléments 
# s=sum(L[0:k])=8   # somme initiale
# le deuxieme étape consiste à faire glisser la fenêtre de taille k à travers la liste
#s=1+5+1=7
#s=5+1+3=9
#donc la somme maximale est 9 

def sum_subarray(L, k):
    n=len(L)
    max_sum=0
    if n<k:
        return None
    for i in range(n - k + 1): # parcourir chaque sous-tableau de taille k le dernier tableau est necessairement a l'indice n-k
        current_sum=0
        for j in range(i,i+k): # parcourir les k éléments du sous-tableau
            current_sum+=L[j] 
            if current_sum>max_sum:
                max_sum=current_sum
    return max_sum
L=[2,1,5,1,3,2]
k=3
print(sum_subarray(L, k))

# def max_sum_subarray(arr, k):
#     # somme des k premiers éléments
#     window_sum = sum(arr[:k])
#     max_sum = window_sum
    
#     # glisser la fenêtre
#     for i in range(k, len(arr)):
#         window_sum += arr[i] - arr[i-k]
#         max_sum = max(max_sum, window_sum)  
#     return max_sum


print("=== Probleme Best time to Buy and Sell Stock ===")

def maxProfit(prices):
    min_price = float('inf')  # Initialiser le prix minimum à l'infini
    max_profit = 0            # Initialiser le profit maximum à 0
    for price in prices:
        # Mettre à jour le prix minimum si le prix actuel est inférieur
        if price < min_price:
            min_price = price
        # Calculer le profit potentiel si on vendait au prix actuel
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit 

print(maxProfit([7,1,5,3,6,4]))  # Output: 5 (Acheter à 1 et vendre à 6)



print("Version Ameliorer")
def Besttime(L):
    left, n = 0, len(L)
    right, profit = 1, 0
    while right < n:
        current_profit = L[right] - L[left]
        profit = max(profit, current_profit)
        # si le prix à droite est plus bas, on déplace le pointeur gauche
        if L[right] < L[left]:
            left = right   
        right += 1
    return profit 
print(Besttime([7,1,5,3,6,4]))  # Output: 5 (Acheter à 1 et vendre à 6)