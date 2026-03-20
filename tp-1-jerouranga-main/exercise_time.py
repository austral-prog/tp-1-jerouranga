def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """

    total_segundos = 3665
    total_horas = 3665//(60**2)
    print(total_horas)
    minutos_restantes = (3665%(60**2))//60
    print(minutos_restantes)
    segundos_restantes = (3665%(60**2))%60
    print(segundos_restantes)

