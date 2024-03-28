### TD3




class Tree():


    def __init__(self, label, *children):
        """Create a Tree named label with the list children for children"""
        self.__label = label
        self.__children = children


    def label(self):
        """Return the label of the Tree as a string"""
        return str(self.__label)


    def children(self):
        """Return the children as a tuple"""
        return tuple(self.__children)

    def nb_children(self):
        """Return the number of child of a Tree """
        number = 0
        children = self.children()

        for child in children :
            if type(child) == Tree:
                # print(type(child))
                number += child.nb_children() +1
            else:
                # print(type(child))
                number += 1
        return number


    def child(self,i):
        """ Return the i-th subTree"""
        if type(i) != int:
            raise ValueError("i must be integer")

        children = self.children()

        if len(children) < i:
            raise ValueError("i is greater than ",len(children))

        child_i = children[i-1]
        if type(child_i) == Tree:
            return child_i
        else:
            Child_i_tree = Tree(child_i)
            return Child_i_tree






    def is_leaf(self):
        """Test if the Tree has children or no"""
        children_number = self.nb_children()
        if children_number == 0:
            return True
        else:
            return False


    def depth(self):
        """Return the depth of a Tree  """

        children = self.children()
        # print(children)
        if len(children) == 0 :
            return 0
        children_depth = [0]
        for child in children:
            if type(child) == Tree:
                children_depth.append(child.depth())

        return 1 + max(children_depth)


    def __str__(self):
        """Return the string representing the Tree"""
        string = self.label()
        #print("number of character ", self.nb_children() + 1)
        if self.is_leaf() == True :    # leaf case
            return string
        string += '('
        children = self.children()
        for child in children:
            if type(child) == Tree:
                string += child.__str__() + ','
            if type(child) == str:
                string += child + ','
        if string[-1] == ',':
            string = string[:-1]
        string += ')'
        return string

    def __eq__(self, __value):
        """Test the equality of two Tree and return the corresponding bool """
        if type(__value) != Tree:
            raise ValueError("__value must be a Tree")

        if self.__str__() == __value.__str__():
            return True

        else:
            return False




    def deriv(self,var):
        """Derive a polynome represented by a Tree with "var" as the variable, leaf must be Tree """
        if type(var) != str:
            raise ValueError("var must be a string")


        result_children = []
        children = self.children()


        if self.label() == '*':

            child_label=[]
            for child in children:
                child_label.append(child.label())
            #print(child_label)
            exponent = child_label.count(var)
            #print(exponent)
            children = list(children)
            result_child = children
            result_child.append(Tree(exponent))
            result_child.remove(Tree(var))
            return Tree('*', *result_child)

        if self.label() == var:
            return Tree('1')



        for child in children:
            if type(child) == Tree:
                if child.label() == '*':

                    L = child.deriv(var)
                    result_children.append(L)
            else :
                raise ValueError("Every node must be a Tree")

        if len(result_children) == 0:
            # in case that we derived a constant Tree, like Tree('1')
            return Tree('0')

        return Tree('+', *result_children)


















if __name__ == '__main__':

    tree1 = Tree('a', *['b', 'c'])
    assert type(tree1) == Tree
    # print(type(tree1))
    # print(tree1.label())
    # print(tree1.children())
    tree2 = Tree('g',*[tree1,'t'])
    # print(type(tree2.label()))
    # print(tree2.label())
    #print(tree2.children())
    assert tree2.nb_children() == 4      # Test for a 4 children Tree
    tree3=Tree('v',*[])
    assert tree3.nb_children() == 0      # Test for the child number of a leaf
    assert tree3.is_leaf()
    assert tree2.child(1).label() == 'a'         # Test for a non-leaf child
    assert tree2.child(2).label() == 't'         # Test for a leaf
    assert tree2.depth() == 2                    # depth test
    assert tree3.depth() == 0
    assert tree1.depth() == 1
    tree4=Tree('m',*[tree2,tree1,'h',tree3])
    assert tree4.depth() == 3
    assert tree1.__str__() == 'a(b,c)'
    assert tree2.__str__() == 'g(a(b,c),t)'
    assert tree3.__str__() == 'v'
    assert tree4.__str__() == 'm(g(a(b,c),t),a(b,c),h,v)'
    assert not tree1.__eq__(tree2)
    assert tree4.__eq__(tree4)


    # Derivation test of a polynome type a*X**b

    tree12=Tree('*',*[Tree('2'),Tree('X'),Tree('X'),Tree('X')])
    tree13 = tree12.deriv('X')
    assert tree13.__str__() == "*(2,X,X,3)"

    # Derivation test of 3*X*X + 5*X + 7

    var=Tree('X')
    tree5 = Tree('+',*[Tree('*',*[Tree('3'),var,var]),Tree('*',*[Tree('5'),var]),Tree('7')])
    assert tree5.__str__() == '+(*(3,X,X),*(5,X),7)'
    tree6 = tree5.deriv('X')
    assert tree6.__str__() == '+(*(3,X,2),*(5,1))'

    # Derivation test of a constant polynome like 2

    tree7 = Tree('2')
    tree8 = tree7.deriv('X')
    assert tree8.__str__() == '0'




