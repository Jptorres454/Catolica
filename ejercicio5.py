print("============================================")
print("\n Ejercicio N°4 \n")
print("============================================")

print("Digita dos numero para ver si no divisores o no ")
num_uno = int(input("Ingrese un numero: "))
num_dos = int(input("Ingrese otro numero :D: "))

if num_uno%num_dos == 0:
    print(num_uno, " es divisor de ", num_dos)
else:
    print(num_uno, " no es divisor de ", num_dos)