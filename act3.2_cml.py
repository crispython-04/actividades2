numero = int(input("Introduce un numero mayor que 1: "))

while numero < 2:
    numero = int(input("Introduce un numero mayor que 1: "))

es_primo = True
divisor = 2

while es_primo and divisor < numero:
    if numero % divisor == 0:
        es_primo  = False
    else:
        divisor += 1

if es_primo:
    print(f"El {numero} es primo")
else:
    print(f"El {numero} no es primo")