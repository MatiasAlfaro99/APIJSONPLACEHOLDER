from crud_api import CRUDAPI

def mostrar_datos(endpoint, sort_key=None, limit=5):
    """Muestra los registros de un endpoint, ordenados por una clave específica."""
    data = CRUDAPI.get_data(endpoint, sort_key=sort_key)
    for item in data[:limit]:
        for key, value in item.items():
            print(f"{key}: {value}")
        print("\n" + "-" * 40 + "\n")  # Separador entre registros


def main():
    while True:
        print("\nMenú Principal:")
        print("1. Ver /posts (ordenar por 'id')")
        print("2. Ver /comments (ordenar por 'postId')")
        print("3. Ver /albums (ordenar por 'title')")
        print("4. Ver /photos (ordenar por 'id')")
        print("5. Ver /todos (ordenar por 'completed')")
        print("6. Ver /users (ordenar por 'name')")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_datos("posts", sort_key="id")
        elif opcion == "2":
            mostrar_datos("comments", sort_key="postId")
        elif opcion == "3":
            mostrar_datos("albums", sort_key="title")
        elif opcion == "4":
            mostrar_datos("photos", sort_key="id", limit=10)
        elif opcion == "5":
            mostrar_datos("todos", sort_key="completed")
        elif opcion == "6":
            mostrar_datos("users", sort_key="name")
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
