import json
import requests
import emoji

def main():
    x=0
    while x==0:
        contacts=requests.get("http://demo7130536.mockable.io/contacts")
        convertir=json.loads(contacts.text)
        print("CONTACT BOOK")
        print("------------------")
        print("MENÚ PRINCIPAL")
        opcion=int(input("""
        1.Agregar Contactos
        2.Ver Contactos
        3.Editar Contactos
        4.Llamar contacto
        5.Enviar Mensaje
        6.Salir\n """))
        print("------------------")
        #Agregar Contacto
        if opcion==1:
            name=input("Ingrese el nombre del contacto\n")
            numero=int(input("Ingrese el número de telefono\n"))
            email=input("Ingrese el correo electronico de la persona\n")
            letra=name[0]
            contacto = {f'{letra}':[{'nombre': f'{name}', 'telefono': f'{numero}', 'email': f'{email}'}]}
            print(contacto)
            convertir.append(contacto)
        #Ver contactos
        elif opcion==2:
            print (json.dumps(convertir, indent=4, sort_keys=True)) 
        #Editar Contactos
        elif opcion==3:
            input("Escribe el nombre del contacto que desea editar")
        elif opcion==4:
            print (json.dumps(convertir, indent=4, sort_keys=True)) 
            llamar=input("Escribe el nombre de la persona que deseas llamar\n")
            letra1=llamar[0]
            if llamar in convertir:
                print(emoji.emojize(f":telephone_receiver: Llamando"))
            else:
                print("No está")
        #Enviar Mensaje
        elif opcion==5:
            print("A quien desea enviarle mensaje")  
        elif opcion==6:
            print("Saliendo...")
            x=1 
main()