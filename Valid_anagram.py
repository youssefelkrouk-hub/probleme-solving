s="yyoussef"
count={}
for elt in s :
    count[elt]=count.get(elt,0)+1
print(count)

# this fonction count the occurence of each elment in the string 
# and return the results on a dinctionary format
# keys are elment  , value are the occurence
# another alternative  is to do the following : 

count2={}
for elt in s:
    if elt in count2:
        count2[elt]+=1
    else:
        count2[elt]=1
print(count2)

print("\n")

#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
def isAnagram(s, t):
        if len(s)!=len(t):
            return False
        countT,countS={},{}

        for i in range(len(s)):
            countT[t[i]]=countT.get(t[i],0)+1
            countS[s[i]]=countS.get(s[i],0)+1
        return countT==countS

s = "anagram"
t = "nagaram"
print("Using a hash map to count each character with his occurence : ",isAnagram(s,t),"\n")





    