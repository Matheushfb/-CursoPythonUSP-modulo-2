import Triangulo

class TestTriangulo:
    def teste_perimetr_1(self):
        t = Triangulo.Triangulo(1,1,1)
        assert t.perimetro() == 3
    def teste_perimetr_2(self):
        t = Triangulo.Triangulo(2,1,1)
        assert t.perimetro() == 4
    def teste_perimetr_3(self):
        t = Triangulo.Triangulo(30,30,30)
        assert t.perimetro() == 90