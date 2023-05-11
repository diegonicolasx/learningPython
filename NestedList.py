# Declaración de funciones
# Captura los valores de la matriz
def captura_datos(m,n,mat):
    print ("Ingrese datos numéricos:")
    for i in range(m): # Recorrido por filas
        mat.append([]) #Agregamos una fila vacía
        for j in range(n): # Recorrido por columnas
            venta = float(input("Matriz["+str(i+1)+"]["+str(j+1)+"] : "))
            mat[i].append(venta)
            
# Expone los valores de la matriz
def mostrar_matriz(m,n,mat): 
    print("\n\tColumnas")
    print("Filas\t",end="")
    for j in range(n): 
        print(j+1,"\t",end="") # Rotulos de columnas
    print()
    for i in range(m): 
        print(i+1,"\t",end="") # Rotulos de filas
        for j in range(n): # Valores por filas
            print(round(mat[i][j],2),"\t",end="")
        print()

# Muestra la suma de las filas
def suma_filas(m,n,mat,suma_fil):
    for i in range(m):
      sumador2 = 0.0
      for j in range(n):
        sumador2 = sumador2 + mat[i][j]
      print("Suma de la fila ", i+1,": ",sumador2)
      suma_fil.append(sumador2)

# Muestra la suma de las columnas
def suma_columnas(m,n,mat,suma_col):
    for j in range(n): # Recorrido por columnas
        sumador = 0.0
        for i in range(m): # Recorrido por filas
            sumador = sumador + mat[i][j]
        print("Suma de la columna ",j+1,": ",sumador)
        suma_col.append(sumador)
        
# Muestra la mayor suma de filas
def mayor_filas(suma_fil):
    mayor_suma2 = max(suma_fil)
    num_fila = (suma_fil.index(mayor_suma2) + 1)
    print("Fila con mayor suma: ", num_fila," con un monto de; ",mayor_suma2)

# Muestra la mayor suma de columnas
def mayor_columnas(suma_col):
    mayor_suma = max(suma_col)
    num_columna = (suma_col.index(mayor_suma) + 1)
    print("Columna con mayor suma: ",num_columna," con un monto de: ",mayor_suma)

# Programa principal   
op=0
while (op!=7):
    print("\nOperaciones sobre una matriz")
    print("1. Llenar la matriz")
    print("2. Mostrar la matriz")
    print("3. Sumar filas")
    print("4. Sumar columnas")
    print("5. Mayor suma de filas")
    print("6. Mayor suma de columnas")
    print("7. Salir del programa")
    op = int(input("Indique la opción: "))
    if (op==1):
        matriz = [] # Inicialización de la matriz
        m = 0 # número de filas
        n = 0 # número de columna
        m = int(input("Ingrese el número de filas (máximo 100): "))
        n = int(input("Ingrese el número de columnas (máximo 100): "))
        captura_datos(m,n,matriz)
    elif (op==2):
        mostrar_matriz(m,n,matriz)
    elif (op==3):
        suma_fil = []
        suma_filas(m,n,matriz,suma_fil)
    elif (op==4):
        suma_col = []
        suma_columnas(m,n,matriz,suma_col)
    elif (op==5):
        mayor_filas(suma_fil)
    elif (op==6):
        mayor_columnas(suma_col)
    elif (op==7):
        print("\nPrograma terminado...")
    else:
        print("\nOpción inválida!!!")
