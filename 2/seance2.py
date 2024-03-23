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



    def __init__(self, numerator, denominator):
        """Create a Fraction if the inputs allow it"""
        if not type(numerator) == int:
            raise ValueError("Numerator must be integer")
        if not type(denominator) == int or denominator == 0:
            raise ValueError("denominator must be a non-zero integer")
        self.__numerator = numerator
        self.__denominator = denominator



    # def set_fraction(self, numerator, denominator):
    #     self.set_numerator(numerator)
    #     self.set_denominator(denominator)
    #


    def numerator(self):
        """numerator return the numerator of a fraction"""

        return self.__numerator

    def denominator(self):
        """denominator return the denominator of a fraction"""
        return self.__denominator

    def to_string(self):
        """Return a string representing the fraction"""
        return"(%s/%s)" %(self.numerator(), self.denominator())
    #ex2
    def add(self, fraction2):
        """add addition two fractions and return a third fraction which is the addition"""
        denominator1 = self.denominator()
        denominator2 = fraction2.denominator()
        numerator1 = self.numerator()
        numerator2 = fraction2.numerator()

        denominator_sum = denominator1 * denominator2
        numerator_sum = numerator1 * denominator2 + numerator2 * denominator1
        fraction_sum=Fraction(numerator_sum, denominator_sum)
        return fraction_sum

    def mult(self, fraction2):
        """mult multiply two fractions and return a third fraction which is the multiplication"""
        denominator1 = self.denominator()
        denominator2 = fraction2.denominator()
        numerator1 = self.numerator()
        numerator2 = fraction2.numerator()

        fraction_mult=Fraction(numerator1 * numerator2, denominator1 * denominator2)
        return fraction_mult

    # equality
    def __eq__(self, fraction2):
        """__eq__ tests the equality of two fractions and return a bool"""
        denominator1 = self.denominator()
        denominator2 = fraction2.denominator()
        numerator1 = self.numerator()
        numerator2 = fraction2.numerator()
        if denominator1 == denominator2 and numerator1 == numerator2:
            return True
        else:
            return False


    def simplify(self):
        """Simplify a fraction by modifying it"""
        denominator1 = self.denominator()
        numerator1 = self.numerator()


        pgcd = m.gcd(denominator1, numerator1)

        self.__init__(int(numerator1/pgcd), int(denominator1/pgcd))











if __name__ == '__main__':
    fraction1 = Fraction(1, 2)
    #fraction1.set_numerator('a')
    #fraction1.set_denominator(0)
    #fraction1.set_denominateur('a')
    assert fraction1.to_string() == '(1/2)'    # Display and definition check
    fraction2 = Fraction(1, 3)
    assert fraction2.to_string() == '(1/3)'    # Display and definition chek
    fraction1=fraction1.add(fraction2)
    assert fraction1.to_string() == '(5/6)'    # Addition check
    fraction1=fraction1.mult(fraction2)
    assert fraction1.to_string() == '(5/18)'    # Multiplication check
    fraction3=Fraction(5, 18)
    assert fraction1.__eq__(fraction3) == True     # Equality check
    #  Simplify function check
    fraction4 = Fraction(10, 15)
    fraction4.simplify()
    assert fraction4.to_string() == '(2/3)'





### Exercise 3

h0=Fraction(1, 1)
iterations = 10000
for k in range (2, iterations+1):
    fractionk = Fraction(1,k)
    h0 = h0.add(fractionk)
    h0.simplify()

h0.simplify()
print("The exercise 3 answer is  ", h0.to_string())

### Exercise 4

leibniz = Fraction(0, 1)
iterations = 10000
for k in range (0, iterations+1):
    fractionk = Fraction((-1)**k, 2*k+1)
    leibniz = leibniz.add(fractionk)
    leibniz.simplify()
leibniz.simplify()
print("The exercise 4 answer is ", leibniz.to_string())











