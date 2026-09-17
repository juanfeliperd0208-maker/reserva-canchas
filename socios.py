socios = []

def registrar_socio(nombre, documento):
    socios.append({"nombre": nombre, "documento": documento})
    print(f"Socio {nombre} registrado correctamente")

def listar_socios():
    print("--- SOCIOS REGISTRADOS ---")
    for s in socios:
        print(f"{s['documento']} - {s['nombre']}")