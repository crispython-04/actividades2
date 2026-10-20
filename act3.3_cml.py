producto = 170
pagado = 0
monedas_aceptadas = [10, 20, 50, 100]
cambio_centimos = 0
cambio_euros = 0

while pagado < producto:
    moneda = int(input("Introduce una moneda: "))

    if moneda in monedas_aceptadas:
        pagado += moneda
        print(f"Llevas pagado {pagado}")
    else:
        print("La moneda no es válida")

cambio_centimos = pagado - producto
cambio_euros = cambio_centimos /100

print(f"Cambio a devolver en euros: {cambio_euros} €")
print(f"Cambio a devolver en centimos: {cambio_centimos} cént.")