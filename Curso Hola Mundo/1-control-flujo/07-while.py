num = 1

# while num < 100:
#     print(num)
#     num *= 2

# command = ""

# while command.lower() != "salir":
#     command = input("$ ")
#     print(command)

while True:
    command = input("$ ")
    print(command)              # ctrl + c -> salir de loop infinito
    if command.lower() == "salir":
        break
