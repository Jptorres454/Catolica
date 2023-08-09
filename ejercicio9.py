print("============================================")
print("\n Ejercicio N°9 \n")
print("============================================")

nombre = input("Digita tu nombre: ")

print("========================================================================")
print("Vamos a calificar tu promedio atravez de 3 notas de 1.0 a 5.0: ")
print("========================================================================")

a = float(input("Cuanto sacaste en Programacion: "))
b = float(input("Cuanto sacaste en Lenguas "))
c = float(input("Cuanto sacaste en Calculo: "))

promedio = (a + b + c)/3
promedio =round(promedio, 2)
print("========================================================================")

print("Tu resultado es: ", promedio)

if promedio >= 3.0:
    print("Pasaste :D")
elif promedio < 3.0:
    print("No pasaste D:")