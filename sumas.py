#def sumar(a:int = 0,b:int = 0) -> int:
def sumar(a=0,b=0):    
    return a+b

resultado = sumar(5,3)
print(f'resultado de la suma es: {resultado}')
print(f'El resultado de la suma es {sumar(5,4)}')

