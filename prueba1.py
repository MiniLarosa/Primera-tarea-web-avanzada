def calcular_pago(dia, horas, minutos):
    tarifas = {
        'lunes': 2.00,
        'martes': 2.00,
        'miércoles': 2.00,
        'jueves': 2.50,
        'viernes': 2.50,
        'sábado': 3.00,
        'domingo': 3.00
    }
    
    if dia.lower() in tarifas:
        if 0 <= horas <= 24 and 0 <= minutos < 60:
            tiempo_total = horas + minutos / 60
            tiempo_total = max(tiempo_total, 0.25)  
            horas_a_pagar = int(tiempo_total) + (1 if tiempo_total % 1 > 0.0833 else 0)
            total_a_pagar = tarifas[dia.lower()] * horas_a_pagar
            print(f"Total a pagar: ${total_a_pagar:.2f}")
        else:
            print("Tiempo ingresado incorrecto.")
    else:
        print("Día incorrecto.")

dia_semana = input("Ingrese el día de la semana: ")
horas_estacionado = int(input("Ingrese las horas estacionado: "))
minutos_estacionado = int(input("Ingrese los minutos estacionado: "))

calcular_pago(dia_semana, horas_estacionado, minutos_estacionado)
