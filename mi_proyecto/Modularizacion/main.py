# Importamos las funciones específicas desde el paquete y módulo finanzas.py
from utilidades.finanzas import calcular_iva, aplicar_descuento

precio_producto = 50.0
precio_rebajado = aplicar_descuento(precio_producto, 10)
precio_final = calcular_iva(precio_rebajado)

print(f"Precio original: {precio_producto}€")
print(f"Total a pagar tras descuento e IVA: {precio_final:.2f}€")