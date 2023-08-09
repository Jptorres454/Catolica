print("============================================")
print("\n Ejercicio N°6 \n")
print("============================================")
def num_mcd(a, b):
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

mcd = num_mcd(num1, num2)
print(f"El MCD de {num1} y {num2} es {mcd}.")
