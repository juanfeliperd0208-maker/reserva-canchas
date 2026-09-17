reservas = []

def reservar_cancha(cancha, socio, hora):
    reservas.append({"cancha": cancha, "socio": socio, "hora": hora})
    print(f"{cancha} reservada para {socio} a las {hora}")

def listar_reservas():
    print("--- RESERVAS ACTIVAS ---")
    for r in reservas:
        print(f"{r['hora']} - {r['cancha']} - {r['socio']}")