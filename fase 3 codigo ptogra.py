print("HOLA BIENVENIDO")

def mostrar_menu():
    print ("1. Jugar")
    print("2. Niveles")
    print("3. Instrucciones")
    print("4. Salir")
def instrucciones():
    print("\n--- INSTRUCCIONES ---")
    print("Corre por el escenario.")
    print("Responde preguntas para superar obstáculos.")
    print("Cada respuesta correcta te da una manzana.")
    print("Si fallas, perderás una manzana.")
    print("Completa los 30 niveles para ganar.\n")
def niveles():
    print("\n--- NIVELES ---")
for i in range(1, 31):
    print("Nivel", i)
print()
def jugar():
    print("\n¡Comienza la aventura!\n")
def principal():
    while True:
        mostrar_menu()
opcion = input("Selecciona una opción: ")
if opcion == "1":
    jugar()
elif opcion == "2":
    niveles()
elif opcion == "3":
    instrucciones()

elif opcion == "4":
    print("Gracias por jugar.")
else:
        print("Opción no válida.\n")
principal()