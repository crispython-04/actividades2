letras = {}
palabra = input("Dime la palabra ").lower().strip()

for letra in palabra:
    if letra not in letras:
        letras[letra] = palabra.count(letras)

print(letras)