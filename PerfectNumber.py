# Función número perfecto.
def perfect(n):
  f = 0
  # Calcular los divisores de un número.
  for i in range (1, n):
    if (n % i == 0):
      f = f + i
    else:
      f
  if (f == n):
    return True
  else:
    return False


# Programa principal.
print("Número perfecto.")
n = int(input("Indique un número natural: "))
if perfect(n):
  print("El número ingresado SI es perfecto")  
else:
  print("El número ingresado NO es perfecto
