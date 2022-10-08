import TipoTriangulo

class TestTipoTriangulo:
    def teste_lado_1(self):
        t = TipoTriangulo.TipoTriangulo(1,1,1)
        assert t.tipo_lado() == 'equilátero'
    def teste_lado_2(self):
        t = TipoTriangulo.TipoTriangulo(2,1,1)
        assert t.tipo_lado() == 'isósceles'
    def teste_lado_3(self):
        t = TipoTriangulo.TipoTriangulo(30,20,10)
        assert t.tipo_lado() == 'escaleno'