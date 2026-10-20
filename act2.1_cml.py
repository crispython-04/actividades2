import random

operacion = input("¿Qué operación desea realizar: ingresar, retirar, consultar? ")
operacion_limpia = operacion.lower().strip()
saldo = random.randint(0,1000)
estado = True

match operacion_limpia:
    case "ingresar":
        cantidad = int(input("Dinero a ingresar: "))
        if cantidad > 0:
            saldo += cantidad
            else:
                print("Cantidad no válida")
            case "retirar":
            cantidad = int(input("Dinero a retirar: "))
        if cantidad > 0 and cantidad <= saldo:
                saldo -= cantidad
            else:
                print("Cantidad no válida")
        case "consultar":