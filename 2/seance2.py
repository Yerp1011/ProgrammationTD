### TD2

### import

import math as m


###Personal comment
# Put some assert

# Raise ValueError('Denominator must be non-zero')

# Put a sectin for tests  if _name_='_main_':

# Look at @property

###



class Fraction:
    #ex1
    def _init_(self, numerator, denominator):
        self.__numerator = set_numerator(numerator)
        self.__denominator = set_denominator(denominator)
        self.value = "(%s/%s)" %(numerator, denominator)


    def set_numerator(self, numerator):

        if not type(numerator) == int:
            raise ValueError("Numerator must be integer")
        self.__numerator = numerator

    def set_denominator(self, denominator):

        if not type(denominator) == int or denominator == 0:
            raise ValueError("denominator must be a non-zero integer")
        self.__denominator = denominator



    def set_fraction(self, numerator, denominator):
        self.set_numerator(numerator)
        self.set_denominator(denominator)



    def numerator(self):
        return self.__numerator

    def denominator(self):
        return self.__denominator

    def get_fraction(self):
        return"(%s/%s)" %(self.numerator(), self.denominator())
    #ex2
    def add(self, fraction2):
        denominator1 = self.denominator()
        denominator2 = fraction2.denominator()
        numerator1 = self.numerator()
        numerator2 = fraction2.numerator()

        denominator_sum = denominator1 * denominator2
        numerator_sum = numerator1 * denominator2 + numerator2 * denominator1
        self.set_numerator(numerator_sum)
        self.set_denominator(denominator_sum)

    def mult(self, fraction2):
        denominator1 = self.denominator()
        denominator2 = fraction2.denominator()
        numerator1 = self.numerator()
        numerator2 = fraction2.numerator()

        self.set_numerator(numerator1 * numerator2)
        self.set_denominator(denominator1 * denominator2)

    # equality
    def __eq__(self, fraction2):
        denominator1 = self.denominator()
        denominator2 = fraction2.denominator()
        numerator1 = self.numerator()
        numerator2 = fraction2.numerator()
        if denominator1 == denominator2 and numerator1 == numerator2:
            return True
        else:
            return False


    def simplify(self):
        denominator1 = self.denominator()
        numerator1 = self.numerator()


        pgcd = m.gcd(denominator1, numerator1)

        self.set_fraction(int(numerator1/pgcd), int(denominator1/pgcd))











if __name__ == '__main__':
    fraction1 = Fraction()
    fraction1.set_numerator(1)
    fraction1.set_denominator(2)
    #fraction1.set_numerator('a')
    #fraction1.set_denominator(0)
    #fraction1.set_denominateur('a')
    assert fraction1.get_fraction() == '(1/2)'    # Display and definition check
    fraction2 = Fraction()
    fraction2.set_numerator(1)
    fraction2.set_denominator(3)
    assert fraction2.get_fraction() == '(1/3)'    # Display and definition chek
    fraction1.add(fraction2)
    assert fraction1.get_fraction() == '(5/6)'    # Addition check
    fraction1.mult(fraction2)
    assert fraction1.get_fraction() == '(5/18)'    # Multiplication check
    fraction3=Fraction()
    fraction3.set_numerator(5)
    fraction3.set_denominator(18)
    assert fraction1.__eq__(fraction3) == True     # Equality check
    #  Simplify function check
    fraction4 = Fraction()
    fraction4.set_fraction(10, 15)
    fraction4.simplify()
    assert fraction4.get_fraction() == '(2/3)'





### Exercise 3

h0=Fraction()
h0.set_fraction(1, 1)
iterations = 10000
for k in range (2, iterations+1):
    fractionk = Fraction()
    fractionk.set_fraction(1, k)
    h0.add(fractionk)
    h0.simplify()

h0.simplify()
print("The exercise 3 answer is  ", h0.get_fraction())

### Exercise 4

leibniz = Fraction()
leibniz.set_fraction(0, 1)
iterations = 10000
for k in range (0, iterations+1):
    fractionk = Fraction()
    fractionk.set_fraction((-1)**k, 2*k+1)
    leibniz.add(fractionk)
    leibniz.simplify()
leibniz.simplify()
print("The exercise 4 answer is ", leibniz.get_fraction())











