import re
import os
import subprocess
CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = {}
    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                name, phone, email = line.strip().split(" | ")
                contacts[name] = {"Teléfono": phone, "Correo": email}
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    sorted_contacts = sorted(contacts.items(), key=lambda
    x: x[0].lower())
    with open(CONTACTS_FILE, "w", encoding="utf-8") as file:
        for name, info in sorted_contacts:
            file.write(f"{name} | {info['Teléfono']} | {info['Correo']}\n")

    if os.name == "nt": # Windows
        os.startfile(CONTACTS_FILE)
    elif os.name == "posix":
        if 'Darwin' in os.uname(): # MacOS
            subprocess.Popen(['open', CONTACTS_FILE]) 
        else: # Linux
            subprocess.Popen(['xdg-open', CONTACTS_FILE])

def add_contact():
    flag = False
    while not flag:
        stay = input(f"¿Deseas agregar un usuario? (si/no): ").lower()
        if stay == "si":
            name = input("Nombre: ").strip()
            phone = input("Teléfono: ").strip()
            email = input("Correo: ").strip()
            if not name or not phone or not email:
                print("Lo siento, no puedes dejar campos vacíos.")
            else:
                contacts = load_contacts()
                if name in contacts:
                    print("Lo siento, este contacto ya existe.")
                else:
                    contacts[name] = {"Teléfono": phone, "Correo": email}
                    save_contacts(contacts)
                    print("Tu nuevo contacto ha sido agregado correctamente.")
                    flag = True
        else:
            return

def show_contacts():
    stay = input(f"¿Deseas ver contactos guardados? (si/no): ").lower()
    if stay == "si":
        contacts = load_contacts()
        if not contacts:
            print("Ups!, no hay contactos guardados.")
        else:
            for name, info in contacts.items():
                print(f"{name} - {info['Teléfono']} - {info['Correo']}")
    else:
        return

def clean_name(name):
    return re.sub(r'[^\w\s]', '', name).lower()

def search_contact():
    flag = False
    while not flag:
        stay = input(f"¿Deseas buscar un contacto? (si/no): ").lower()
        if stay == "si":
            search_term = input("Por favor, ingresa el nombre o parte del nombre que deseas buscar: ")
            contacts = load_contacts()

            search_term_clean = clean_name(search_term)

            found = False
            for name, info in contacts.items():
                name_clean = clean_name(name)
                if search_term_clean in name_clean:
                    print(f"{name} - {info['Teléfono']} - {info['Correo']}")
                    found = True
                    flag = True
            if not found:
                print("Lo siento, no se encontraron contactos con ese nombre.")
        else:
            return

def update_contact():
    flag = False
    while not flag:
        stay = input(f"¿Deseas actualizar un contacto? (si/no): ").lower()
        if stay == "si":
                name = input("Por favor ingresa el nombre del contacto que deseas actualizar: ")
                contacts = load_contacts()

                if name in contacts:
                    change_name = input(f"¿Desea cambiar el nombre de {name}? (si/no): ").lower()
                    
                    if change_name == "si":
                        new_name = input("Ingrese el nuevo nombre: ")
                        save_name = input(f"¿Estás seguro de que deseas cambiar el nombre de {name} a {new_name}? (si/no): ").lower()
                        if save_name == "si":
                            contacts[new_name] = contacts.pop(name)  
                            name = new_name 
                    phone = input("Ingresa nuevo teléfono (deja en blanco para conservar el actual): ")
                    email = input("Ingresa nuevo correo (deja en blanco para conservar el actual): ")

                    if phone:
                        contacts[name]["Teléfono"] = phone
                    if email:
                        contacts[name]["Correo"] = email

                    save_changes = input("¿Estás seguro de que deseas guardar los cambios? (si/no): ").lower()
                    if save_changes == "si":
                        save_contacts(contacts)
                        print("Listo!, tu contacto ha sido actualizado correctamente.")
                        flag = True
                else:
                    print("Una disculpa, no he podido encontrar el contacto solicitado.")
        else:
            return

def delete_contact():
    flag = False
    while not flag:
        stay = input(f"¿Deseas eliminar un contacto? (si/no): ").lower()
        if stay == "si":
            name = input("Por favor, ingresa el nombre del contacto que deseas eliminar: ")
            contacts = load_contacts()

            if name in contacts:
                delete = input(f"¿Estás seguro de que deseas eliminar a {name}? (si/no): ").lower()
                if delete == "si":
                    del contacts[name]
                    save_contacts(contacts)
                    print("Listo!, tu contacto ha sido eliminado correctamente.")
                    flag = True
                else:
                    print("No se ha eliminado el contacto.")
                    flag = True
            else:
                print("Ups!, contacto no encontrado.")
        else:
            return

def delete_agenda():
    delete = input("¿Estás seguro de que deseas eliminar todos los contactos? (si/no): ").lower()
    if delete == "si":
        with open(CONTACTS_FILE, "w") as file:
            pass
        print("Listo!, tu agenda ha sido eliminada correctamente.")

def menu():
    while True:
        print("\nAGENDA DE CONTACTOS")
        print("1. Agregar contacto nuevo")
        print("2. Ver contactos guardados")
        print("3. Buscar contacto")
        print("4. Actualizar contacto")
        print("5. Eliminar contacto")
        print("6. Eliminar agenda")
        print("7. Salir")

        option = input("Hola, por favor elije una opción: ")

        if option == "1":
            add_contact()
        elif option == "2":
            show_contacts()
        elif option == "3":
            search_contact()
        elif option == "4":
            update_contact()
        elif option == "5":
            delete_contact()
        elif option == "6":
            delete_agenda()
        elif option == "7":
            confirm_exit = input("¿Seguro que deseas salir? (si/no): ").lower()
            if confirm_exit == "si":
                print("¡Nos vemos pronto!\nSaliendo del programa...")
                break
        else:
            print("Lo siento, esa opción no es válida. Por favor intenta de nuevo.")

if __name__ == "__main__":
    menu()