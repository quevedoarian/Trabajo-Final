import random, pickle, os, sys

archivo_tickets = "tickets.pkl"


if os.path.isfile(archivo_tickets):
    with open(archivo_tickets, "rb") as f:
        tickets = pickle.load(f)
else:
    tickets = {}


def guardar_tickets():
    with open(archivo_tickets, "wb") as f:
        pickle.dump(tickets, f)

# Función Alta de Tickets
def Alta_Ticket():
    escape = False
    while not escape:
        nombre = input("Indique su nombre: ")
        sector = input("Indique su sector: ")
        asunto = input("Indique el asunto: ")
        problema = input("Indique si tiene algún problema: ")

        # Genero un número random:
        numero_random = random.randrange(1000, 9999)

        # Guardo los datos del ticket creado en el diccionario
        tickets[numero_random] = {
            "Nombre": nombre,
            "Sector": sector,
            "Asunto": asunto,
            "Problema": problema
        }

        # Guardar en el archivo
        guardar_tickets()

        # Mostrar el ticket
        print("\nTicket")
        print(f"Su nombre: {nombre} \t Número de Ticket: {numero_random}")
        print(f"Sector: {sector}")
        print(f"Asunto: {asunto}")
        print(f"Problema: {problema}")

        opcion = input("¿Desea salir? (s/n): ").strip().lower()
        if opcion == "s":
            escape = True

# Función Leer Tickets
def leer_ticket():
    escape = False
    while not escape:
        print("\n\t---- Lectura de Ticket ----")
        try:
            numero_ticket = int(input("Ingrese su número de ticket: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if numero_ticket in tickets:
            print("\tInformación sobre el ticket:")
            info_ticket = tickets[numero_ticket]
            print(f"Nombre: {info_ticket['Nombre']}")
            print(f"Sector: {info_ticket['Sector']}")
            print(f"Asunto: {info_ticket['Asunto']}")
            print(f"Problema: {info_ticket['Problema']}")
        else:
            print("Número de Ticket Inexistente\n")

        opcion = input("¿Desea leer otro ticket? (s/n): ").strip().lower()
        if opcion == "n":
            print("Volviendo al menú principal\n")
            escape = True

# Función Menú Principal
def main_menu():
    salir = False
    while not salir:
        print("\n1. Alta de ticket")
        print("2. Leer un ticket")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            Alta_Ticket()
        elif opcion == "2":
            leer_ticket()
        elif opcion == "3":
            respuesta = input("¿Desea salir del menú? (s/n): ").strip().lower()
            if respuesta == "s":
                print("Guardando cambios y saliendo del programa...")
                guardar_tickets()
                sys.exit()
            elif respuesta == "n":
                print("Regresando al menú de inicio...")
            else:
                print("La opción es incorrecta, intente nuevamente.")
        else:
            print("La opción es incorrecta, por favor, vuelva a intentarlo.")

# Llamada a la función del menú principal
main_menu()

        
        
        
        
        
        
        
        
        