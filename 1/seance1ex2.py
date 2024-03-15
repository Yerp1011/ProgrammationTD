#### Séance de TD n°1 Ex2

f=open("frenchssaccent.dic",'r')

list=f.readlines()

List2=[]

for i in list :
    List2.append(i[0:-1])
#print(L)

def the_longest(words):
    max=0
    word_max=0
    for word in words:
        if len(word)>max:
            max=len(word)
            word_max=word
    return word_max


print(the_longest(List2))