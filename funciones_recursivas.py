# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

resultado = factorial(5)

print(f'El resultado del factorial 5 es {resultado}')


### Ejerecicio para usar funciones recursivas y decrecer el número dado:

def numeroRecursivo(numero):
    if numero >= 1:
        print(numero)
        numeroRecursivo(numero-1)
    elif numero == 0:
        return
    elif numero < 0:
        print('El valor es incorrecto')

numeroRecursivo(10)