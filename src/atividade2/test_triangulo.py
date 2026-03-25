import pytest
from calculo_triangulo import classifica_triangulo  

def test_triangulo_equilatero():
    assert classifica_triangulo(5, 5, 5) == 'equilátero'

def test_triangulo_isosceles():
    assert classifica_triangulo(5, 5, 8) == 'isósceles'

def test_triangulo_escaleno():
    assert classifica_triangulo(3, 4, 5) == 'escaleno'

def test_triangulo_invalido():
    with pytest.raises(ValueError) as excinfo:
        classifica_triangulo(1, 2, 3)  
    assert "Não forma um triângulo válido" in str(excinfo.value)

def test_triangulo_lados_negativos():
    with pytest.raises(ValueError) as excinfo:
        classifica_triangulo(-1, 2, 3)
    assert "Um triângulo não pode ter lados com comprimento zero ou negativo" in str(excinfo.value)

def test_triangulo_lados_zero():
    with pytest.raises(ValueError) as excinfo:
        classifica_triangulo(0, 0, 0)
    assert "Um triângulo não pode ter lados com comprimento zero ou negativo" in str(excinfo.value)

def test_triangulo_no_limite():
    with pytest.raises(ValueError) as excinfo:
        classifica_triangulo(2, 2, 4)  
    assert "Não forma um triângulo válido" in str(excinfo.value)

@pytest.mark.parametrize("a, b, c, tipo_esperado", [
    (5,5,3, 'isósceles'),
    (5,3,5, 'isósceles'),
    (3,5,5, 'isósceles'),
    (10,5,5, ValueError), 
    (10, 5, 5, ValueError),   
    (5, 10, 5, ValueError),   
    (1, 1, 3, ValueError),    
])

def test_triangulo_isoceles_tipos_esperado(a, b, c, tipo_esperado):
    if tipo_esperado == ValueError:
        with pytest.raises(ValueError):
            classifica_triangulo(a, b, c)
    else:
        assert classifica_triangulo(a, b, c) == tipo_esperado