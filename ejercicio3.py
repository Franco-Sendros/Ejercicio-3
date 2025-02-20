"""Si te gustaría unirte a nosotros, postúlate a la búsqueda, para que luego puedas enviarnos la solución del siguiente rompecabezas.
¿Podrías decirnos cuál es el resultado de ejecutar el siguiente pseudocódigo? (suponiendo que la máquina tiene los recursos suficientes para completar su ejecución). Por favor, no te olvides de explicarnos cuál fue tu proceso de pensamiento para llegar al resultado.

const M = 2701

funcion compute(n)
string s = ""
para i desde 1 hasta n
s = s + n
fin para
return convertir_a_numero(s) % M
fin funcion

para cada n en 1, 2, 5, 10, 20, 371844285230994047
imprimir(n + ": " + compute(n))
fin para
fin funcion

Resultado parcial de la ejecución
1: 1
2: 22
5: 1535
10: 1083
20: 1095
371844285230994047: ???

Estamos en la búsqueda de desarrolladores con experiencia para trabajar en la modalidad de home office, con dedicación de tiempo completo y en relación de dependencia. """


"""
print(371844285230994047%divisor)

print(371844285230994047000000000000000000%divisor)

print(371844285230994047000000000000000000000000000000000000%divisor)

print(371844285230994047000000000000000000000000000000000000000000000000000000%divisor)

print(371844285230994047000000000000000000000000000000000000000000000000000000000000000000000000%divisor)

print(371844285230994047000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000%divisor)

array = [1920,1032,1365,2253]  encontre este patron"""

#funcion que obtiene el resto de restos de n.(k-1).10^18 concatenado k veces
def obtenerModulo(k):
    divisor = 2701
    array = [1920,1032,1365,2253]
    if k == 1:
        return array[0]
    if k <= 0:
        return 0
    
    resto = array[0]
    indice = 1
    for i in range(1 , k):
        resto = (resto + array [indice]) % divisor
        indice += 1
        if indice == 4:
            indice = 0
    
    return resto

print("Probando primera funcion... (restos de n.(k-1).10^18) ")
print(f"k=1 : {obtenerModulo(1)}" )
print(f"k=2 : {obtenerModulo(2)}" )
print(f"k=3 : {obtenerModulo(3)}" )
print(f"k=4 : {obtenerModulo(4)}" )
print(f"k=5 : {obtenerModulo(5)}" )




print("datos de primera funcion (restos de s = s + n)")
print(obtenerModulo(149))
print(obtenerModulo(512))
print(obtenerModulo(2321))
print(obtenerModulo(21323))

#luego de encontrar que 371844285230994047 concatenado 148 veces es un ciclo donde se repiten los restos
#creo una funcion que obtimiza la primera

def obtenerModulo2(n):
    m = n % 148 #numeros de ciclos de el modulo
    if n > 147 and m == 0:
        return obtenerModulo(148)
    return obtenerModulo(m)

print("probando la funcion optimizada... (restos de s = s + n)")
print(obtenerModulo2(149))
print(obtenerModulo2(512))
print(obtenerModulo2(2321))
print(obtenerModulo2(21323))

#al verificar que sirve la segunda funcion la utilizo para obtener el resultado
print(f"371844285230994047 mod 2701 es: {obtenerModulo2(371844285230994047)}")






        
