"""
Funciones y valores utilizados en el codigo cesar
"""
list_of_variables=[["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
"k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w" ,"x", "y", "z"],["á","é","í","ó","u","a","e","i","o","u"],
[".",",","!","¡",":","@","[","]","-","+","€"," "],
["1","2","3","4","5","6","7","8","9","0","-1","-2","-3","-4","-5","-6","-7","-8","-9","-0"]]




def to_list(input):
    """ convierte una cadena en una lista de strings"""
    list_input=list(input)
    return list_input

def index_list_strings(list_input, var_list):
    """
Permite obtener los indices de cada string dentro de una lista
dos bucles primer bucle miro dentro de var list
segundo bucle miro dentro de cada lista de var list y
busco si esta o no esta la string
retorna una lista con indices [0,0]
primer indice corresponde a la sublista de variables donde esta, el segundo
corresponde a la posicion de la string dentro de esa lista
si no encuentra una cadena compatible con lo que se le ingresa no lo procesara pero no 
dara error, devolverá cadena vacia
"""
    index_list=[]
    
    for i in list_input:
        for var in var_list:
                if i in var:
                    index_list.append([var_list.index(var),var.index(i)])
                    break
    return index_list


def move_index(index_list,displace):
     """
Recibe: Una lista de listas con indices ej: [[0,1],[1,2]]
y un numero de veces a las que hay que desplazar los indices

Hace: Desplaza el segundo valor de la lista con indices ej: [0,1] desplazamiento 3  ---> [0,4]

Devuelve: Una lista de listas con los indices desplazados
"""
     new_index_list=[]
     for index in index_list:
          new_index=index[1]
          new_index+=displace
          new_index_list.append([index[0],new_index])    
          
     return new_index_list  

def recompose_list_string(new_index_list,var_list):
 """
 Recibe una lista de listas de indices y una lista de listas de variables
 Convierte los indices de listas en sus correspondientes dentro de listas de variables

 -Si es positivo y dentro del indice ira por el else
 -si es positivo pero fuera del indice, le restara la longitud de la lista hasta dar con un valor
   dentro de su indice
 -si es negativo pero dentro del indice lo convertira a positivo y luego invertira la lista de variables
   para simular que la recorre al reves
 -si es negativo y fuera del indice restara la longitud de la cadena y luego invertira la lista 
  de variables

  retorna una lista de strings
 """
 recompose=[]
 for index in new_index_list:
  if index[1]>=len(var_list[index[0]]):#mayor que la longitud de la lista
      initial_index=index[1]
      while True:        
        correctect_index=initial_index-(len(var_list[index[0]]))
        if correctect_index<=len(var_list[index[0]]):
            recompose.append(var_list[index[0]][correctect_index-1])   
            break   
        initial_index=correctect_index

  elif index[1]<0: #detecta que el indice es menor que cero
       positive_index=(index[1]*-1)
       reverse_var=list(reversed(var_list[index[0]]))
       if positive_index<=len(var_list[index[0]]): #menor que cero pero dentro de la longitud de la lista
           recompose.append(reverse_var[positive_index-1])  
       elif positive_index>=len(var_list[index[0]]):     
                  
        while True:
         correctect_index=positive_index-(len(var_list[index[0]]))
         if correctect_index<=len(var_list[index[0]]): #menor que cero y mayor que la longitud de la lista
            recompose.append(reverse_var[correctect_index-1])   
            break 
         positive_index=correctect_index
               

  else:
      recompose.append(var_list[index[0]][index[1]])
 return recompose


def concatenate_list(list_strings):
    """
    Recibe una lista de caracteres y devuelve una cadena con la union de todos los de la lista
    """
    result=""
    for i in list_strings:
        result+=i
    return result


def cesar():
 """ Le pide al usuario una cadena"""
 string=input("¿Qué deseas cifrar? ").lower()
 move=int(input("¿Cuanto nos desplazamos? "))
 original_index=index_list_strings(to_list(string),list_of_variables)
 new_index=move_index(original_index,move)
 return concatenate_list(recompose_list_string(new_index,list_of_variables))
 




 


     

    
            
        



