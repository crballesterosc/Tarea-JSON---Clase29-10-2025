import json

data = {
    "Persona1":{
        "nombres": "Juan Antonio",
        "apellidos": "Diaz Coronado",
        "edad":19,
        "colombiano":True,
        "deportes":["Futbol","Ajedrez","Gimnasia"]
    },
    "Persona2":{
        "nombres": "Dorotea Maritza",
        "apellidos": "Luna Sol",
        "edad":25,
        "colombiano":False,
        "deportes":["Baloncesto","Ajedrez","Gimnasia"]
    },
    "Persona3":{
        "nombres": "Juan Alejandro",
        "apellidos": "Avila Hernandez",
        "edad":23,
        "colombiano":True,
        "deportes":["Futbol","Ajedrez","Gimnasia"]
    },
    "Persona4":{
        "nombres": "Sofia",
        "apellidos": "Bernal Garcia",
        "edad":20,
        "colombiano":False,
        "deportes":["Baloncesto","Ajedrez","Gimnasia"]
    },
    "Persona5":{
        "nombres": "Miguel Angel",
        "apellidos": "Galindo Rubio",
        "edad":26,
        "colombiano":True,
        "deportes":["Futbol","Ajedrez","Gimnasia"]
    }
}

def INIT():
    def WRITE():
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    def READ():
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    WRITE()
    READ()

print("Tarea - JSON")
print("Bienvenido a mis ejercicios - Autor: Cristian Ballesteros")
INIT()
a = 1


while(a <= 2):
    a += 1
    print("\n")
    opcion = int(input("Digite el numero del problema que desea revisar: "))
    print("\n")
    print(f"Problema {opcion}\n")

    def Problema1():
        b = 0
        while(b < 2):
            b += 1
            sportg = []
            print("Deportes: Futbol - Baloncesto")
            deporteB = str(input("Ingrese un deporte: ")).strip().lower()
            
            for person in data.values():
                deportes = [d.lower() for d in person.get("deportes", [])]
                if deporteB in deportes:
                    nombre_completo = f"{person['nombres']} {person['apellidos']}"
                    sportg.append(nombre_completo)
                    
            if sportg:
                print(f"\nPersonas que practican {deporteB.capitalize()}:")
                for name in sportg:
                    print("-", name)
                print("\n")
            
            else:
                print(f"\nNo se encontraron personas que practiquen {deporteB}.")
                print("\n")

    def Problema2():
        peopleage = []
        edadMIN = int(input("Ingrese el minimo de edad: "))
        edadMAX = int(input("Ingrese el maximo de edad: "))   
        print(f"\nPersonas entre {edadMIN} y {edadMAX} años:\n")
        found = False
        for person, info in data.items():
            if edadMIN <= info["edad"] <= edadMAX:
                nombre_completo = f"{info['nombres']} {info['apellidos']}"
                peopleage.append(nombre_completo)
                found = True
        if not found:
            print(f"No hay personas en el rango de {edadMIN} - {edadMAX} años")
        
        if peopleage:
                for name in peopleage:
                    print("-", name)
                print("\n")
    
    
    if(opcion == 1):
        Problema1()
    elif(opcion == 2):
        Problema2()
    else:
        print("Opcion no valida :(")
