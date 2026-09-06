# String are immutable : remeber that also tuple "tupl=(1,2,3,4)" in python are immutable , inchangeabale    
# h= "Python"
# h[0] = "J" 
# this code will genrate an error:TypeError: 'str' object does not support item assignment

s = "Python"
print(id(s))     # ex: 140234567891232

s += "!"
print(id(s))     # ex: 140234567895104   ← diffrent memroy adress wich mean s doesn't point on s !

print("\n")

j="YOUSSEF DATA"
b="".join(char for char in j )
print(b)

print("\n")
## Anther way to create a string based on anothe roe 
empty_string=""
for s in j:
    empty_string+=s
print(empty_string)


c=[1,2,3,4,5]
a=c
a.append(6)
print(c)
# List are mutable : we can change it after creation : 

print(id(c))  
print(id(a))
# Same id which mean a , b point to the some data type object in the  memory 
print("\n")


# 1. La base : joindre une liste de mots

mots = ["Python ", "est ", "genial"] # we will this  to solve this problem 
resultat ="".join(mots)
print(resultat)
# another way :
stat=""
for s in mots:
    stat+=s+""
print(stat,"\n")



# the remove vowyelles problem solution : 


def removevowelles(s):
    Vowels="aeiou"
    output=[]
    for elt in s:
        if elt not in Vowels:
            output.append(elt)
    return "".join(output)

s="youssef"
print(removevowelles(s),"\n")

j="aeiou"
print(removevowelles(j)) #return anything 

def one_line_remove_vowels(s):
    return "".join([c for c in s if c not in "aeiou"])

q="youssef"
print(one_line_remove_vowels(q),"\n")
