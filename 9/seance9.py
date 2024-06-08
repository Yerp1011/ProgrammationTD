### TD 9




class Polynome:
    def __init__(self, n, q, coef_list):
        """Create a polynome in Z_q[x]/(x^n+1)Z_q[x] """
        for coef in coef_list:
            if type(coef) != int:
                raise ValueError("every coefficient must be an int")

        for i in range(len(coef_list)):
            coef_list[i] = coef_list[i] % q

        self.__q = q
        self.__n = n
        self.__coef_list = coef_list
        self.euclidian_division()

        for i in range(len(self.__coef_list)):
            self.__coef_list[i] = self.__coef_list[i] % q






    def euclidian_division(self):
        """Realize the euclidian division of a polynome by X**n + 1 """
        if len(self.__coef_list) > self.__n:

            remain = []

            # P = alpha(X) * X**n + beta(X),   deg(beta(X))<n
            # alors : P === beta(X) - alpha(X) [X**n + 1]
            beta = []
            alphaxn = self.__coef_list.copy()   # = alpha*X**n
            for i in range(self.__n):
                beta.append(alphaxn[i])
                alphaxn[i] = 0
            alpha = alphaxn[self.__n:]
            # print(self.__coef_list)
            # print(alpha)
            # print(beta)

            for i in range(min(len(alpha), len(beta))):
                remain.append(beta[i] - alpha[i])

            if len(alpha) < len(beta):
                for i in range(len(beta)-len(alpha)):
                    remain.append(beta[i + len(alpha)])
            elif len(alpha) > len(beta):
                for i in range(len(alpha)-len(beta)):
                    remain.append(alpha[i + len(beta)])

            #print(remain)

            self.__coef_list = remain
            self.euclidian_division()



    def add(self, polynome):
        """Create a new polynome, addition of the two polynome in input """
        if self.__n != polynome.__n:
            raise ValueError("n1 != n2")
        if self.__q != polynome.__q:
            raise ValueError("q1 != q2")

        result = [0 for i in range (self.__n)]
        for i in range(self.__n):
            result[i] = (self.__coef_list[i] + polynome.__coef_list[i]) % self.__q

        return Polynome(self.__n, self.__q, result)


    def mult(self, polynome):
        """Multiply two polynome and create a polynome in result """
        if self.__n != polynome.__n:
            raise ValueError("n1 != n2")
        if self.__q != polynome.__q:
            raise ValueError("q1 != q2")

        coef_list1 = self.__coef_list
        coef_list2 = polynome.__coef_list

        result = [0 for i in range(len(coef_list1) + len(coef_list2))]
        for i in range(len(coef_list1)):
            for j in range(len(coef_list2)):
                result[i + j] += coef_list1[i] * coef_list2[j]
        return Polynome(self.__n, self.__q, result)




    def to_str(self):
        """Represent a polynome by a string object """
        result = ""
        j = 0
        for i in range(len(self.__coef_list)):
            coef = self.__coef_list[i]
            if coef != 0:
                if i == 0:
                    result += str(coef) + '+'
                else:
                    result += str(coef) + f"X**{j}" + "+"
            j+=1

        return result[:-1]

    def scalar(self, c):
        """Create a new polynome by multiplying the input polynome by a scalar """
        coef_list = self.__coef_list
        for  i in range(len(coef_list)):
            coef_list[i] = coef_list[i] * c
        return Polynome(self.__n, self.__q, coef_list)

    def rescale(self, r):
        """Change the value of q that define the Polynome """
        coef_list = self.__coef_list
        return Polynome(self.__n, r, coef_list)


    def fscalar(self, r, alpha):
        """Multiply the polynome by alpha and rescale it by changing the value of q by r  """
        result = [0 for i in range(len(self.__coef_list))]
        for i in range(len(self.__coef_list)):
            result[i] = round(self.__coef_list[i] * alpha)
        # print(self.__coef_list)
        # print(result)
        return Polynome(self.__n, r, result)




if __name__ == '__main__':
    P = Polynome(5, 5, [0, 2, 1, 0, 9])
    assert P.to_str() == "2X**1+1X**2+4X**4"

    R = Polynome(4, 5, [0, 2, 1, 0, 9])
    assert R.to_str() == "1+2X**1+1X**2"
    F = Polynome(3, 5, [-1, 0, 2, 1, 0, 2])
    assert F.to_str() == "3"

    Q = Polynome(4, 5, [0, 4, 1, 0, 0])
    M = Polynome(4, 5, [0, 2, 1, 0, 0])
    D = Q.add(M)
    assert D.to_str() == "1X**1+2X**2"

    W = Q.mult(M)
    assert W.to_str() == "4+3X**2+1X**3"

    L = W.scalar(2)
    assert L.to_str() == "3+1X**2+2X**3"

    L1 = L.rescale(2)
    assert L1.to_str() == "1+1X**2"

    L2 = L1.fscalar(3, 13.5)
    assert L2.to_str() == "2+2X**2"






























