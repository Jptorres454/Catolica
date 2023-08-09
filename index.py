#Ejercicio 2


"""nombre = input("Introduce tu nombre: ")
print("Hola " + nombre + ", vamos a sacar el area de un triangulo.")

num_uno = int(input("Introduce cuanto vale la base: "))
num_dos = int(input("Introduce cuanto vale la altura: "))

resultado = (num_uno * num_dos)/2

print(nombre + " tu resultado es: ", resultado)
"""

#Ejercicio 3

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Ejemplo de uso
numero = int(input("Ingresa un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
