"""
Crear una función cifradora que permita que una letra en el texto original es 
reemplazada por otra letra que se encuentra un número fijo de posiciones más adelante 
en el alfabeto


-entrada texto
-cada letra sera un valor dentro de una lista
-lista abecedario
-detectar que letra es y su posicion
-sumar el incremento de letras
-si excede al indice recalcular para que no exceda
-rehacer la cadena con una nueva

"""
from cesar_functions import cesar
if __name__=="__main__":
    print(cesar())
