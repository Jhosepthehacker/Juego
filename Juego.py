#python 3.12
while True:
    nombre = input("Hola Jugador ¿Cómo te llamas?: ")
    print(f"Hola {nombre} Bienvenido A Este Juego De Adventura")
    jugando = input(f"Estás Caminando En Una Ciudad Abandonada Y Destruida Por Causa De Una Guerra. De Repente Consigues 4 Caminos Uno Te Lleva A Una Farmacia Abandonada Otra te Lleva A Una Casa Abandonada Y Otra te lleva A Un Laboratorio Abandonado ¿Qué Camino Elijes {nombre} la A Farmacia Abandonada, la B La Casa Abandonada, o la C El Laboratorio Abandonado?: ")
    if jugando.lower() == a:
        print("LLegas A La Farmacia Y Ves Que Hay Medicamentos Que Todavía Sirven. En Ese Momento Te Das Cuenta Que La Guerra Y La Destrucción Fué Reciente")
    elif jugando.lower() == b:
        print("Llegas A La Casa Abandonada Y Descubres Que Está En Buen Estado Por Adentro")
    elif jugando.lower() == c:
        print("Llegas Al Laboratorio Y Te sientes Muy Mal Al Entrar Sientes Mareos Náuseas Y Sientes Que Estás A Punto De Desmayarte. Incluso Sientes Que No Puedes Respirar")
    else:
        print("No Es Una Respuesta Válida")
