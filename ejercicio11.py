print("========================================================================")
print("\n Ejercicio N°11 \n")
print("========================================================================")

numero = int(input("Digite un numero entero: "))

respuesta = numero % 2

if respuesta == 0:
    print("El ", numero, " es par.")
elif respuesta == 1: 
    print("El ", numero, " es impar.")

print("Fin.")