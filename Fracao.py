class Fracao:
    numerador = 1
    denominador = 1

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def add(self, fracao):
        num = (self.numerador * fracao.denominador) + (fracao.numerador *
                                                       self.denominador)
        den = (self.denominador * fracao.denominador)
        return Fracao(num, den)

    def sub(self, fracao):
        if (self.denominador
                == fracao.denominador) & (self.numerador != fracao.numerador):
            num = (self.numerador - fracao.numerador)
            den = (self.denominador)
            return Fracao(num, den)
        elif (self.denominador == fracao.denominador) & (self.numerador
                                                         == fracao.numerador):
            num = 0
            den = 0
            return Fracao(num, den)
        else:
            num = (self.numerador * fracao.denominador) - (fracao.numerador *
                                                           self.denominador)
            den = (self.denominador * fracao.denominador)
        return Fracao(num, den)

    def mul(self, fracao):
        num = (self.numerador * fracao.numerador)
        den = (self.denominador * fracao.denominador)
        return Fracao(num, den)

    def simplify(self):
        for i in range(2, 10):
            if (self.numerador % i == 0 and self.denominador % i == 0):
                self.numerador = self.numerador / i
                self.denominador = self.denominador / i
                return f"{self.numerador}/{self.denominador}"
            else:
                print("nao é possivel simplificar")
        return

    def solve(self):
        return self.numerador / self.denominador

    def str(self):
        return f"{self.numerador}/{self.denominador}"
