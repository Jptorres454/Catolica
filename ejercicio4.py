print("============================================")
print("\n Ejercicio N°4 \n")
print("============================================")


num_uno = int(input("Ingrese el salario del profesor: "))

if num_uno < 18000:
    incremento = num_uno * 0.08
else:
    if num_uno >= 18000 and num_uno <= 30000:
        incremento = num_uno * 0.07
    else:
        incremento = num_uno * 0.06

nuevoSalario = num_uno + incremento
print("Nuevo salario es: ", nuevoSalario)