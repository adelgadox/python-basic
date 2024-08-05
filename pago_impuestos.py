# Formula = pago total = pago sin impuestos + pago sin impuestos * (impuesto/100)

def calcularImpuestos(pagoSinImpuesto, porcentajeImpuesto):
    pagoTotal = 0
    
    if pagoSinImpuesto > 0:
        pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (porcentajeImpuesto/100)
        return pagoTotal
    
pagoSinImpuestos = float(input('Proporcione el monto de pago sin impuesto: '))
porcentaje = float(input('Proporcione el monto del impuesto a aplicar: '))

pagoConImpuestos = calcularImpuestos(pagoSinImpuestos,porcentaje)

print(f'El pago total va a ser de {pagoConImpuestos}')