n1 = input("Ingresa primer número: ")
n2 = input("Ingresa segundo número: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Suma de {n1} + {n2} = {suma}.
Resta de {n1} - {n2} = {resta}.
Multiplicación de {n1} * {n2} = {multi}.
División de {n1} / {n2} = {div}.
"""

print(mensaje)
