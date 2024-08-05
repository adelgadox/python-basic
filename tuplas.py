#Se usa el asterisco cuando no se define una cantidad de valores en el argumento. Llamados "Argumentos variables"

def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

def sumarValores(*args):
    #Se agrega la palabra reservada pass para poder continuar luego la función
    #pass
    resultado = 0
    #Se itera cada elemento y se va almacenando en la variable resultado.
    for valor in args:
        resultado += valor
    return resultado

def multiplicarValores(*args):
    resultado = 1
    for valor in args:
        #resultado = resultado * valor
        resultado *= valor
    return resultado

listarNombres('Pedro','Juan','Maria','Jose')
print(f'Los valores suman un total de {sumarValores(3,5,9)}')
print(f'Los valores multiplicados dan un total de {multiplicarValores(3,5,9)}')

######## Tuplas con llave Valor

# Se utiliza ** para indicar que habrán dos valores (llave, valor). Python hace referencia a ellos como "kargs"

#Podrian enviarse varios argumentos de diferentes tipos (fijos, listas, diccionario)
#def listarTerminos(nombre, *nombres, **terminos):
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'La llave {llave} tiene el valor {valor}')

listarTerminos(IDE='Integrated Development Environment', PK='Primary Key', DBMS='Database Management System')