def validar_valor_x(valor_str):
    """
    Valida que el valor ingresado para x sea un número real.
    Retorna float o lanza ValueError si no es válido.
    """
    try:
        valor = float(valor_str)
        return valor
    except ValueError as e:
        raise ValueError("El valor de x debe ser un número real.") from e
