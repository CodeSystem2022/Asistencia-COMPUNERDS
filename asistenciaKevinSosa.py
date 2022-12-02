# Ejercicio 1: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego meter los caracteres en una lista sin repetir caractres
cadena = input('Ingrese una Palabra: ')
lista = {'',}
for i in cadena:
    letra = i
    lista.add(letra)
lista.remove('')
list(lista)
print(lista)

