def classifica_triangulo(a, b, c):
  if (a <= 0 or b <= 0 or c <= 0):
    raise ValueError("Um triângulo não pode ter lados com comprimento zero ou negativo")

  if a + b <= c or a + c <= b or b + c <= a:
    raise ValueError("Não forma um triângulo válido")
  
  if (a - b >= c or a - c >= b or b - c >= a):
    raise ValueError("Não forma um triângulo válido")

  if (a == b and b == c):
    return 'equilátero'

  if (a == b or b == c or a == c):
    return 'isósceles'
  
  return 'escaleno'