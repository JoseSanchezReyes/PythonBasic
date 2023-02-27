animal = "CerDito feLiz"
print(animal.upper())                       # CERDITO FELIZ
print(animal.lower())                       # cerdito feliz
print(animal.strip().capitalize())          # Cerdito feliz
print(animal.title())                       # Cerdito Feliz
print(animal.strip())  # CerDito FeLiz <Quita los espacios del string>
print(animal.lstrip())  # Quita espacios de la izquierda del string
print(animal.rstrip())  # Quita los espacios de la derecha del string
print(animal.find("Di"))                    # 4
print(animal.find("DI"))                    # -1 <No encontro el indice>
print(animal.replace("feLiz", "FELIZ"))     # CerDito FELIZ
print("Di" in animal)                       # True
print("Di" not in animal)                   # False
