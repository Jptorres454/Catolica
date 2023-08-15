print("============================================")
print("\n Ejercicio N°3 \n")
print("============================================")


num_uno = int(input("Ingrese el numero de minutos transcurridos: "))
num_dos = int(input("Ingrese el numero de segundos transcurridos: "))
num_tres = int(input("Ingrese el numero de centésimas de segundos: "))

tiempo_transcurrido = (num_uno * 60) + num_dos + (num_tres / 100)

distancia = float(input("Ingrese la distancia en metros: "))

velocidad = distancia / tiempo_transcurrido
velocidad_k = velocidad * 3.6

print("La velocidades: ", round(velocidad_k, 2), "Km/h")