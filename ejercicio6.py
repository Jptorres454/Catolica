print("============================================")
print("\n Ejercicio N°4 \n")
print("============================================")

def calcular_serie(N):
    suma = 0
    signo = 1
    
    for i in range(1, N + 1):
        suma += (i ** i) * signo
        signo = -signo
    
    return suma

N = int(input("Ingrese un número entero N: "))

resultado = calcular_serie(N)
print("El resultado de la serie es:", resultado)
