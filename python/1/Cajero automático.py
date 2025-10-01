# 1. Variables para contar billetes (inventario inicial)
billetes_1000 = 10
billetes_500 = 10
billetes_200 = 10
billetes_100 = 10
billetes_50 = 10

# 3. Mensaje de inicio y solicitud del monto
print("\n--- Dispensadora de Billetes ---")
print("\nBilletes disponibles: $1000, $500, $200, $100, $50.")
# Solicitar monto
monto_str = input("\nIngrese el monto a retirar: ")
monto = int(monto_str)

# Validar si el monto es un múltiplo de 50
if monto % 50 != 0:
    print("\nError: Por favor, ingrese un monto en múltiplos de $50.")
else:
    # Copias del inventario para no modificar el original hasta confirmar la transacción
    temp_billetes_1000 = billetes_1000
    temp_billetes_500 = billetes_500
    temp_billetes_200 = billetes_200
    temp_billetes_100 = billetes_100
    temp_billetes_50 = billetes_50
    
    monto_restante = monto

    # Calcular cuántos billetes se necesitan de cada denominación
    entregar_1000 = min(monto_restante // 1000, temp_billetes_1000)
    monto_restante -= entregar_1000 * 1000
    
    entregar_500 = min(monto_restante // 500, temp_billetes_500)
    monto_restante -= entregar_500 * 500
    
    entregar_200 = min(monto_restante // 200, temp_billetes_200)
    monto_restante -= entregar_200 * 200

    entregar_100 = min(monto_restante // 100, temp_billetes_100)
    monto_restante -= entregar_100 * 100
    
    entregar_50 = min(monto_restante // 50, temp_billetes_50)
    monto_restante -= entregar_50 * 50

    # Comprobar si se puede dispensar el monto exacto
    if monto_restante == 0:
        # De ser posible, se actualiza el inventario real
        billetes_1000 -= entregar_1000
        billetes_500 -= entregar_500
        billetes_200 -= entregar_200
        billetes_100 -= entregar_100
        billetes_50 -= entregar_50
        
        print("\n--- Retiro Exitoso ---")
        print(f"Monto retirado: ${monto}")
        print("\nDesglose de billetes entregados:")
        if entregar_1000 > 0:
            print(f"- {entregar_1000} billete(s) de $1000")
        if entregar_500 > 0:
            print(f"- {entregar_500} billete(s) de $500")
        if entregar_200 > 0:
            print(f"- {entregar_200} billete(s) de $200")
        if entregar_100 > 0:
            print(f"- {entregar_100} billete(s) de $100")
        if entregar_50 > 0:
            print(f"- {entregar_50} billete(s) de $50")
            
        print("\n--- Inventario Restante ---")
        print(f"Billetes de $1000: {billetes_1000}")
        print(f"Billetes de $500: {billetes_500}")
        print(f"Billetes de $200: {billetes_200}")
        print(f"Billetes de $100: {billetes_100}")
        print(f"Billetes de $50: {billetes_50}")

    else:
        # Si no, se informa al usuario
        print("\nOperación cancelada.")
        print("El cajero no cuenta con la combinación de billetes necesaria para su monto.")