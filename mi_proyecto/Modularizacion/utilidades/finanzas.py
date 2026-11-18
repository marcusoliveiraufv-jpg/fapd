def calcular_iva(precio_base, porcentaje=21):
    """Devuelve el precio final con IVA incluido."""
    return precio_base * (1 + porcentaje / 100)


def aplicar_descuento(precio, descuento):
    """Resta un porcentaje de descuento al precio."""
    return precio * (1 - descuento / 100)


# Este bloque solo corre si ejecutas finanzas.py directamente, no cuando lo importas desde main.py
if __name__ == "__main__":
    print("Probando el módulo de finanzas:")
    print(f"100€ con IVA: {calcular_iva(100)}€")