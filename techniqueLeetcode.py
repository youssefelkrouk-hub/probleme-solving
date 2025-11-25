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




