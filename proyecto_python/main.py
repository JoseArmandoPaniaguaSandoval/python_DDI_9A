
""" Proyecto python + mysql
1.- Abrir asistente
2.- Login y registro
3.- si elegimos registro creara un usuario en la bd
4.- si elegimos login identificara al usario y nos preguntara 
5.- crear nota, mostrar notas, o borralas
 """

from usuarios import acciones

print("""
Acciones desponibles
  -registro
  -login
""")

hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?:")

if accion == "registro":
  hazEl.registro()

elif accion == "login":
  hazEl.login()
