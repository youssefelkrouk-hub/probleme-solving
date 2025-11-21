class Persone:
    Max_age=40
    def __init__(self,name,age):
        self.age=age
        self.name=name

perso_1=Persone("Youssef",21)
print(perso_1.name)
print(perso_1.age)