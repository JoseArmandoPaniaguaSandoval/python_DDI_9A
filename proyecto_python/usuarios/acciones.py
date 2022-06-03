from ast import alias
from statistics import mode
import usuarios.usuario as modelo

class Acciones:
    def registro(self):
        print("se procedera a realizar tu registro en el sistema")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("¿Cual es tu email?: ")
        password = input("¿Introduce tu contraseña?: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te as registrado correctamente!!")

           
    def login(self):
       print("\nIdentificate en el sistema...")
      
       try: 
           email = input("Introduce tu email: ")
           password = input("Introduce tu contraseña: ")

           usuario = modelo.Usuario('', '', email, password)
           login = usuario.identificar()
           if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registradoen en el sistema el {5}")
                self.proximasAcciones(login)


       except Exception as e:
          """   print(type(e))
            print(type(e.__name__) """
           
          print("login incorrecto intentelo mas tarde")


    def proximasAcciones(self, usuario):
        print("""
        Aciones disponibles 
         -crear nota (crear)
         -Mostar notas (mostar)
         -Eliminar nota (eliminar)
         Salir (salir)
        """)
        accion = input("¿Que quieres hacer? ")

        if accion == "crear":
            print("vamos a crear nota")
            self.proximasAcciones(usuario)

        elif accion == "mostar":
            print("vamos a mostar")
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            print("vamos a eliminar")
            self.proximasAcciones(usuario)

        elif accion == "salir":
            exit()
    
    
