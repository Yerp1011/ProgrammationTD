#### Seance 1 ex 4



#'zxcvrrt?'


dic={'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,'d': 2, 'g': 2, 'm': 2,'b':3,'c':3,'p':3,'f':4,'h':4,'v':4,'j':8,'q':8,'k':10,'w':10,'x':10,'y':10,'z':10,'?':0}



f=open("frenchssaccent.dic",'r')

list=f.readlines()

List2=[]

for i in list :
    List2.append(i[0:-1])


def score(word):
    pts=0
    for letter in word:
        pts+=dic[letter]
    return pts



def max_score(words):
    max=0
    word_max=0
    for word in words:
        pts=score(word)
        if pts>max:
            max=pts
            word_max=word
    return word_max,max



def occurences(word, character):
    m=0
    for letter in word:
        if letter==character:
            m+=1
    return m




def possible_word_list(characters):
    n=len(characters)
    words=List2.copy()
    # tri sur la longueur du mot
    for word in words:
        if len(word)>n:
            words.remove(word)
    # tri sur les caractères autorisés
    for word in words:
        error=0 #quantifie les écarts entre le mots et les caractères autorisé
        for letter in word:
            if letter not in characters:
                error+=1
        # on autorise qu'un seul joker donc error<=1
        if error>1:
            words.remove(word)
    # à ce stade on peut encore avoir un mot impossible car il utilise 2 fois une lettre que l'on a qu'une seule fois dans notre jeu

    #tri par nombre d'apparition de chaque lettre
    for word in words:
        error=0
        for letter in word:
            necessary=occurences(word,letter) #nombres de caractère letter nécessaire pour le mot
            available=occurences(characters,letter) #nombres de caractère letter disponible
            #on veut disponible>=nécessaire
            if available<necessary:
                error+=necessary-available #on comptabilise les écarts pour déterminer le nombres de joker nécessaire

        if error>1: #mot impossible avec un seul joker
            words.remove(word)
    # à ce stade tous les mots de la liste words sont possible
    return words

L=possible_word_list('zxcvrrt?')
# for l in L:
#     if len(l)>8:
#         print(l)


#print(possible_word_list('zxcvrrt?'))

#print(max_score(possible_word_list('zxcvrrt?')))

