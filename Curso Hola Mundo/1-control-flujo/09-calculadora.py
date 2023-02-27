print("Bienvenidos a la calculadora")
print("Para salir ingresa \"salir\"")
operaciones = """
Para hacer una suma ingresa "+",
Para hacer una resta ingresa "-",
Para hacer una multiplicación ingresa "*",
Para hacer una división ingresa "/",
"""
print(operaciones)

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("ingrese operación: ")
    if op.lower() == ("salir"):
        break
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op == "+":
        resultado += n2
    elif op == "-":
        resultado -= n2
    elif op == "*":
        resultado *= n2
    elif op == "/":
        resultado /= n2
    else:
        print("Operación no valida")
        break

    print(f"El resultado es: {resultado}")
