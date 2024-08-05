
def desplegarNombres(nombres):
    for nombre in nombres:
        print(f'{nombre}')

#Creamos una lista de nombres y la enviamos a la funcion
nombres = ['Pedro','Maria','Federico']
desplegarNombres(nombres)

#Si solo indicamos un string en la funcion, desglosará cada letra del string
desplegarNombres('Carlos')

# No se puede interar valores numéricos
#desplegarNombres(10,11)

# Pero si se agrega parentesis dentro de los valores, se convertirán en tupla y funcionará
desplegarNombres((10,11))

# Para convertirlo en una lista, se agregan corchetes
desplegarNombres([10,11])