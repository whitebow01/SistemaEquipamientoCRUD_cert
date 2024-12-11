from equipamiento import DataBaseMD5 

# Menu general
def menu():
    db = DataBaseMD5()  # Instancia de la clase para manejar la base de datos.

    while True:
        print("\n--- Menú ---")
        print("1. Insertar registro")
        print("2. Login")

        print("3. Mostrar todos los registros")
        print("4. Mostrar registros con precio entre 100000 y 500000")
        print("5. Modificar registro")
        print("6. Eliminar registro")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            db.insertar_registro()
        elif opcion == "2":
            db.login()
        elif opcion == "3":
             db.mostrar_todos()

        elif opcion == "4":
            db.mostrar_rango_precios()
        elif opcion == "5":
            db.modificar_registro()
        elif opcion == "6":
            db.eliminar_registro()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    # Cerramos la conexión al salir del menú.
    db.cursor.close()
    db.conexion.close()

if __name__ == "__main__":
    menu()
