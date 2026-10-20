CODIGO_CORRECTO = "4826"
intentos_restantes = 3

codigo = input("Introduce un codigo")

if codigo == CODIGO_CORRECTO:
    print("Acceso Autorizado")
else:
    while codigo != CODIGO_CORRECTO and intentos_restantes > 1:
        intentos_restantes -= 1
        print(f"El codigo no es correcto")
        codigo = input(f"Vuelve a intentarlo, te quedan {intentos_restantes} intentos: ")

if codigo == CODIGO_CORRECTO:
    print("Acceso Autorizado")

if codigo != CODIGO_CORRECTO:
    print("Acceso bloqueado, no te quedan intentos")