def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    inicio = 0
    fin = len(palabra) - 1
    while inicio < fin:
        if palabra[inicio] != palabra[fin]:
            return False
        inicio += 1
        fin -= 1
    return True

palabra_usuario = input("Ingrese una palabra: ")

if es_palindromo(palabra_usuario):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
