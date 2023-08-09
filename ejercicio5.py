print("============================================")
print("\n Ejercicio N°5 \n")
print("============================================")

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

grds_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
grds_fahrenheit = celsius_a_fahrenheit(grds_celsius)
print(f"{grds_celsius} grados Celsius equivalen a {grds_fahrenheit} grados Fahrenheit.")
