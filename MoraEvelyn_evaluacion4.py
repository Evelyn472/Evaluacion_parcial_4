reservas = {}
stock_maximo = 20

def mostrar_menu():
    print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas")
    print("3.- Ver stock de reservas")
    print("4.- Salir")

def reservar_zapatillas():
    total_reservas = sum(reservas.values())
    if total_reservas >= stock_maximo:
        print("!Sin Stock. No se pueden hacer más reservas¡.")
        return

    nombre = input("Debe ingresar su nombre: ").strip()

    if nombre in reservas:
        print("Este nombre ya tiene una reserva.")
        return

    frase = input("Debe ingresar la frase secreta para continuar: ").strip()

    if frase != "EstoyEnListaDeReserva":
        print("Frase secreta incorrecta. No se pudo realizar la reserva.")
        return

    reservas[nombre] = 1  
    print("!Reserva realizada con exito!.")

def buscar_reserva():
    nombre = input("Debe ingresar el nombre para buscar la reserva: ").strip()
    if nombre in reservas:
        print(f"Reserva encontrada para {nombre}.")
        if reservas[nombre] == 2:
            print("Esta reserva ya es VIP (2 pares).")
            return
        decision = input("¿Desea pagar adicional para la reserva VIP (2 pares)? (s/n): ").lower()
        if decision == 's':
            total_reservas = sum(reservas.values())
            if total_reservas + 1 <= stock_maximo:
                reservas[nombre] = 2
                print("!Reserva VIP realizada con exito¡.")
            else:
                print("Sin stock suficiente para una reserva VIP.")
        else:
            print("No se pudo realizar la mejora a VIP.")
    else:
        print("!Reserva con ese nombre no encontrada¡.")

def ver_stock():
    total_reservas = sum(reservas.values())
    print(f"Total zapatillas reservadas: {total_reservas}")
    print(f"Zapatillas disponibles para reserva: {stock_maximo - total_reservas}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            reservar_zapatillas()
        elif opcion == '2':
            buscar_reserva()
        elif opcion == '3':
            ver_stock()
        elif opcion == '4':
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

main()