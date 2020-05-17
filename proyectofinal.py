import json
import requests
import emoji


def main():
    x=0
    while x==0:
        contacts=requests.get("http://demo7130536.mockable.io/final-contacts-100")
        cjason=contacts.json()
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
            nuevoc={f"{name}":{"telefono":f"{numero}", "email":f"{email}"}}
            letra=name[0]
            for i in cjason:
                if i==letra:
                    for persona in cjason[i]:
                        cjason[letra]=nuevoc
                        print (persona)
            
    
        #Ver contactos
        elif opcion==2:
            n=0
            for l in cjason: 
                print (l+":")
                print("--------------------------------")
                for persona in cjason[l]:
                    n+=1
                    print(f"{n}. {persona}")
                print("--------------------------------")
                print ("\n") 
            letra=input ("Ingrese una letra para filtrar los contactos que desea ver\n")
            for persona in cjason[letra]:
                n+=1
                print("--------------------------------")
                print(f"{n}. {persona}")
                print("--------------------------------")
        
        #Editar Contactos
        elif opcion==3:
            input("Escribe el nombre del contacto que desea editar")
        elif opcion==4: 
            llamar=input("Escribe el nombre de la persona que deseas llamar\n")
            letra1=llamar[0]
            if llamar in cntos[letra1]:
                print(emoji.emojize(f":telephone_receiver: Llamando a {llamar}"))
            else:
                print("No está ese contacto")
        
        #Enviar Mensaje
        elif opcion==5:
            letra5=input("Escriba la primer letra del contacto al que desea enviarle un mensaje\n")
            for i in cjason:
                n=0
                if i==letra5:
                    for p in cjason[i]:
                        n+=1
                        print(f"{n}. {p}")
                    int(input("Escriba el número de persona al que desea enviarle un mensaje"))
    

         
        elif opcion==6:
            print("Saliendo...")
            x=1 
main()