class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # chaque case contient une liste

    def hashing_by_division(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hashing_by_division(key)
        # vérifier si la clé existe déjà
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # sinon, ajouter une nouvelle paire
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hashing_by_division(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hashing_by_division(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# Exemple d’utilisation
def main():
    ht = HashTable(5)  # table de taille 5

    ht.insert(1, "apple")
    ht.insert(6, "banana")  # collision avec 1 (car 6 % 5 = 1)
    ht.insert(11, "cherry") # collision aussi (11 % 5 = 1)
    ht.insert(2, "orange")
#Index 1: [[1, 'apple'], [6, 'banana'], [11, 'cherry']] contient une chaine 
    ht.display()

    print("Recherche clé 6:", ht.search(6))
    ht.delete(11)
    ht.display()


main()


#le chainage sert a resoudre le probléme de collision (deux valeurs correspond aux memes clé ) en introduisant une Linked List : 
#h(x)=key % self.size  function classique de hashage 
#linrae probing : on introduit la nouvelle fonction de hashage h'(x)=[h(x)+i]% size for i=0,i=1,..
#quadratic probing : on introduit h'(x)=[h(x)+i^2]%size for i ... 
