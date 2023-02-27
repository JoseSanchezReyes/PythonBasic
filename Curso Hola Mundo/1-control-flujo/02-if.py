edad = int(input("Ingresa tu edad: "))
if edad > 65:
    print("Puedes ver la película con superdescuento")
elif edad > 54:
    print("Puedes ver la película con descuento")
elif edad > 17:
    print("Puedes ver la película")
else:
    print("No puedes entrar")
