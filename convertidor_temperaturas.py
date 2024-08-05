#funcion que convierte de Celsius a Farenheit

def celsius_a_farenheit(temperaturaCelsius):
    return celsius * 9/5 + 32

def farenheit_a_celsius(temperaturaFarenheit):
    return (temperaturaFarenheit - 32) * 5/9

#Realizar pruebas de conversion:

celsius = float(input('Indica tu valor en Celsius: '))
resultado = celsius_a_farenheit(celsius)

#se indica en resultado a .2f para indicar que solo que solo queremos mostrar 2 decimales
print(f'{celsius} C a F es {resultado:.2f}')

farenheit = float(input('Indica tu valor en Farenheit: '))
resultado = farenheit_a_celsius(farenheit)

print(f'{farenheit} F a C es {resultado:.2f}')