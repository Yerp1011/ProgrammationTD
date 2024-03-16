#### seance 1 ex 3





dic={'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,'d': 2, 'g': 2, 'm': 2,'b':3,'c':3,'p':3,'f':4,'h':4,'v':4,'j':8,'q':8,'k':10,'w':10,'x':10,'y':10,'z':10}

#print(dic)
#print(dic['d'])



def score(word):
    pts=0
    for letter in word:
        pts+=dic[letter]
    return pts


print("score(‘a’) = ", score('a'))
print("score(‘lettre’) = ", score('lettre'))
print("score('scrabble') = ", score('scrabble'))



def max_score(words):
    max=0
    word_max=0
    for word in words:
        pts=score(word)
        if pts>max:
            max=pts
            word_max=word
    return word_max,max

print(max_score(['rte', 'ver', 'ce', 'etc', 'cet', 'ex', 'cr', 'et', 'ter', 'te', 'ct']))



f=open("frenchssaccent.dic",'r')

list=f.readlines()

List2=[]

for i in list :
    List2.append(i[0:-1])

print(max_score(List2))
