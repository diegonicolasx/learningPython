# Introducción a la programación.
# ATDF102.202305.2051.TR.AV
# Autores:
# Alvaro Osorio (RUT: 18.242.152-9)
# Hans Velazquez (RUT: 19.844.388-3) 
# Diego Gallegos (RUT: 18.144.005-8)

# Descripción: Programa que es capaz de tomar pedidos del restorán Pizzarella.
 
# Entrada de datos:
# Primero se le enviará un mensaje de bienvenida a cada cliente que llega:
print("Bienvenido a pizzarella")
total = 0 # Variable usada para calcular el total de la cuenta

# Luego, se le pedirá que indique la cantidad de pizzas que desee...
#... mediante un nuevo mensaje:
p = int(input("Indique la cantidad de pizzas que desea ordenar: "))
        
# A la cantidad de pizzas que ingrese el cliente, se le asociará una condición...
# si no es un número entero positivo, el programa terminará con...
#... un mensaje de orden cancelada:
if (p <= 0): 
        print("Ha ingresado un número que no es válido, la orden fue cancelada.")

# Si la cantidad de pizzas es un número válido, comenzará...
#... la 2darecolección de datos, que son la cantidad de ingredientes:
else:
    for p in range(1, p+1): # Control de pizzas
        i = int(input(f"Ingrese la cantidad de ingredientes de su pizza {p}: "))
        print("1.-Tomate $300")
        print("2.-Piña $500")
        print("3.-Pepperoni $400")   
        print("4.-Aceitunas $600")
        sumador = 1000 # Indicará el valor por pizza
        for i in range(1, i+1): # Control de ingredientes
            a = 0
            while a == 0 or a > 4:
                a = int(input(f'Ingrese el ingrediente {i}: '))
# Proceso:
# Con la entrada de datos terminada comienza el proceso, el cual...
# ... es realizar los calculos para determinar los subtotales y total.
                if a == 1:
                    sumador = sumador + 300
                elif a == 2:
                    sumador = sumador + 500
                elif a == 3:
                    sumador = sumador + 400
                elif a == 4:
                    sumador = sumador + 600
                else:
                    print('Por favor, un ingrediente válido')
        print(f'Subtotal $ {sumador}')
        total = total + sumador    
# Salida:
# La condición de que si el número de pizzas o ingredientes es un...
# ... número par, se aplicará un descuento del 10%.
    if p % 2 == 0 or i % 2 == 0:
        print('Su compra tiene un 10% de descuento')
        descuento = total * 0.9
        descuento = int(descuento)
        print(f'El total es $ {descuento}')
# De no cumplirse la condición, no hay descuento.        
    else:
        print(f'El total es $ {total}')  







    
        
