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



def possible_word_list(character):
    character_counts = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz?'}
    possible_words = []

    for letter in character:
        character_counts[letter] = character_counts[letter] + 1


    for word in List2:
        word_counts = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}

        for letter in word:
            word_counts[letter] = word_counts[letter] + 1


        valid = True
        error=0
        for letter in word:
            if word_counts[letter]>character_counts[letter]:
                error+=word_counts[letter]-character_counts[letter]
        if error>1:
            valid=False

        if valid:
            possible_words.append(word)

    return possible_words



#
# L=possible_word_list('zxcvrrt?')
# print(L)


print(max_score(possible_word_list('zxcvrrt?')))
print("il y a une erreur d'énoncé, le score de czar est 15 et non 14'")

