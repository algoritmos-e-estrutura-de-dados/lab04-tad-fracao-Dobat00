from Fracao import Fracao

fracao1 = Fracao(1, 2)
fracao2 = Fracao(1, 2)
fracao3 = fracao1.add(fracao2)
fracao4 = fracao1.sub(fracao2)
fracao5 = fracao1.mul(fracao2)
fracao6 = fracao1.simplify()
print(f"fracao1: {fracao1}")
print(f"fracao2: {fracao2.solve()}")
print(f"fracao3: {fracao3.solve()}")
print(f"fracao4: {fracao4}")
print(f"fracao5: {fracao5.solve()}")
