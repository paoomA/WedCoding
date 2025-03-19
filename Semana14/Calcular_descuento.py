# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Función para mostrar resultados
def mostrar_resultados(descuento, monto_final):
    print(f"Monto del descuento: ${descuento}")
    print(f"Monto final a pagar: ${monto_final}\n")

# Programa principal
# Primera llamada (10% por defecto)
monto_compra1 = 2000
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1
mostrar_resultados(descuento1, monto_final1)

# Segunda llamada (con 30% de descuento)
monto_compra2 = 2500
descuento2 = calcular_descuento(monto_compra2,30)
monto_final2 = monto_compra2 - descuento2
mostrar_resultados(descuento2, monto_final2)