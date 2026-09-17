from canchas import reservar_cancha, listar_reservas
from socios import registrar_socio, listar_socios
canchas = ["Cancha 1", "Cancha 2", "Cancha 3"]

def mostrar_menu():
    print("=== SISTEMA DE RESERVAS CLUB DE TENIS ===")
    print("1. Ver canchas disponibles")
    print("2. Salir")

mostrar_menu()