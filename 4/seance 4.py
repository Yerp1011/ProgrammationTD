### TD4


# 6 inclu
import matplotlib.pyplot as plt






class Haschtable:
    def __init__(self, function, length):
        """Create a Haschtable with function as haching function """
        self.__function = function
        self.__structure = [[] for i in range (length)]
        # for exercise 4
        self.__collisions = [0 for i in range (length)]



    def resize(self):
        """Create a longer list for the table and reevaluate every position """
        length = len(self.__structure)
        new_table = Haschtable(self.__function, length * 2)
        # print("resizing")
        for structure_input in self.__structure:
            if structure_input != 0:
                new_table.put(structure_input[0], structure_input[1])
        self.__structure = new_table.__structure
        self.__collisions = new_table.__collisions





    def put(self, key, value):
        """Put the tuple (key, value) at its place """

        key_int = self.__function(key) % len(self.__structure)

        # if key_int > len(self.__structure):
        #     raise ValueError("pb")

        if self.__structure[key_int] == []:
            # Writing
            self.__structure[key_int].append((key, value))
            # print('writing first try')
        else:
            couples_number = len(self.__structure[key_int])
            for index_couple in range (couples_number):
                if self.__structure[key_int][index_couple][0] == key:
                    # Overwriting
                    self.__structure[key_int][index_couple] = (key, value)
            if (key,value) not in self.__structure[key_int]:
                #collision
                self.__structure[key_int].append(tuple([key, value]))
                #comptabilisation of collisions
                self.__collisions[key_int] += 1






    def get(self, key):
        """Return the value associated with the key """
        length = len(self.__structure)
        key_int = self.__function(key) % length
        structure = self.__structure
        if structure[key_int] == []:
            #print("not in structure")
            return None
        else:
            couples = structure[key_int]
            for couple in couples:
                if couple[0] == key:
                    return couple[1]
            return None


    def show_structure(self):
        """Return the structure of the Haschtable, a list """
        return self.__structure + []

    def show_collisions(self):
        """Return the collisions list of the Haschtable"""
        return self.__collisions + []

    def repartition(self):
        #☻collisions = self.__collisions
        #x = range(len(collisions))
        structure = self.__structure
        collisions = []
        for element in structure:
            collisions.append(len(element))
        x = range(len(collisions))
        width = 1/1.5
        # plt.title('essai1')
        # plt.bar(x, collisions, width, color = "blue")
        plt.title('Collision Chart')
        plt.bar(x, collisions, width, color = "blue")
        plt.show()
        # print("structure length", len(self.__structure))
        # print("collision length", len(self.__collisions))
        # print("collision sum", sum(self.__collisions))













def hach1(key):
    if type(key) != str:
        raise ValueError("key must be a str")
    result = 0
    for character in key:
        result += ord(character)
    return result



if __name__ == '__main__':
    h = Haschtable(hach1, 3)
    h.put('a',1)
    h.put('b',3)
    h.put('c',9)
    assert h.show_structure() == [[('c', 9)], [('a', 1)], [('b', 3)]]
    #test of overwriting
    h.put('c', 8)
    assert h.show_structure() == [[('c', 8)], [('a', 1)], [('b', 3)]]
    # test of collisions
    h.put('d',9)
    assert h.show_structure() == [[('c', 8)], [('a', 1), ('d', 9)], [('b', 3)]]


    h1 = Haschtable(hach1, 3)
    h1.put('ab',1)
    h1.put('b',3)
    assert h1.show_structure() == [[('ab', 1)], [], [('b', 3)]]
    h1.put('c',11)
    assert h1.show_structure() == [[('ab', 1), ('c', 11)], [], [('b', 3)]]
    h1.put('c',12)
    assert h1.show_structure() == [[('ab', 1), ('c', 12)], [], [('b', 3)]]

    # test of .get
    assert h1.get('ab') == 1
    assert h1.get('k') == None
    h2 = Haschtable(hach1, 3)
    h2.put('ab',1)
    h2.put('b',3)
    assert h2.get('a') == None

    # Test of collision compabilisation
    hc = Haschtable(hach1, 5)
    hc.put('abc', 1)
    hc.put('acb', 2)
    hc.put('bca', 3)
    assert hc.show_collisions() == [0, 0, 0, 0, 2]
    # hc.repartition()


    # exercice 5

    inputs = 320

    file = open("frenchssaccent.dic", 'r')
    file_list = file.readlines()
    file_list1 = []
    for i in file_list :
        file_list1.append(i[0:-1])
    file.close()
    #print(file_list1)

    table_french = Haschtable(hach1, inputs)
    #print(len(table_french.show_structure()), len(table_french.show_collisions()))
    #print(len(file_list1[:inputs]))
    for input in file_list1:
        table_french.put(input, 1)


    collisions_list = table_french.show_collisions()
    collisions_sum = sum(collisions_list)

    table_french.repartition()


















