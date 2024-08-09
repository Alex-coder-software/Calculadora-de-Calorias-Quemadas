
### ¡Calculadora de calorías quemadas por deporte! ###

import json

"""
Calculadora de Calorías Quemadas:

Una herramienta que estima cuántas calorías quemas durante diferentes tipos de ejercicio basado en tu peso y duración del ejercicio.

Deportes Disponibles: Correr, Bicicleta, Natación y Boxeo
"""

def burned_calories():

    condition = True # Definimos esta variable para poder terminar el bucle while

    while condition == True:

        sport = str(input("\nIntroduce el deporte que prácticas. Puedes elegir entre natación, ciclismo, trote o boxeo: "))

        try:

            if sport in ["natación", "natacion", "natacion", "natación"]: # El método "or" daba problemas, sin embargo este método no da problemas

                with open ("spreadsheet.json", "r") as met:

                    sport_time = float(input("\nCuanto ha durado tu sesión de ejercicio en minutos:")) # Preguntamos las variables una vez sabemos el deporte, para que si no está disponible no se pidan
                    weight = float(input("\nIntroduce tu peso: "))

                    data = json.load(met) # Cargamos el json en un diccionario
                    swimming = data["Natacion"] # Logramos el valor del MET desde el diccionario

                    kcal = (swimming * 0.0175) * weight # Fórmula del MET (MET * 0.0175 * peso)
                    kcal_total = kcal * sport_time
                    result = round(kcal_total, 2) # Redondeamos a dos decimales

                print(f"\nTu gasto calórico ha sido de {result} kcal") # Imprimimos resultado

            elif sport in ["ciclismo", "Ciclismo", "bici", "Bici"]: # El método "or" daba problemas, sin embargo este método no da problemas

                with open ("spreadsheet.json", "r") as met:

                    sport_time = float(input("\nCuanto ha durado tu sesión de ejercicio en minutos:")) # Preguntamos las variables una vez sabemos el deporte, para que si no está disponible no se pidan
                    weight = float(input("\nIntroduce tu peso: "))

                    data = json.load(met) # Cargamos el json en un diccionario 
                    cycling = data["Ciclismo"] # Logramos el valor del MET desde el diccionario

                    kcal = (cycling * 0.0175) * weight # Fórmula del MET (MET * 0.0175 * peso)
                    kcal_total = kcal * sport_time
                    result = round(kcal_total, 2) # Redondeamos a dos decimales

                print(f"\nTu gasto calórico ha sido de {result} kcal") # Imprimimos resultado

            elif sport in ["trote", "Trote", "Running", "running"]: # El método "or" daba problemas, sin embargo este método no da problemas

                with open ("spreadsheet.json", "r") as met:

                    sport_time = float(input("\nCuanto ha durado tu sesión de ejercicio en minutos:")) # Preguntamos las variables una vez sabemos el deporte, para que si no está disponible no se pidan
                    weight = float(input("\nIntroduce tu peso: "))

                    data = json.load(met) # Cargamos el json en un diccionario 
                    running = data["Trote"] # Logramos el valor del MET desde el diccionario

                    kcal = (running * 0.0175) * weight # Fórmula del MET (MET * 0.0175 * peso)
                    kcal_total = kcal * sport_time
                    result = round(kcal_total, 2) # Redondeamos a dos decimales

                print(f"\nTu gasto calórico ha sido de {result} kcal") # Imprimimos resultado

            elif sport in ["boxeo", "boxing", "Boxeo", "Boxing"]: # El método "or" daba problemas, sin embargo este método no da problemas

                with open ("spreadsheet.json", "r") as met:

                    sport_time = float(input("\nCuanto ha durado tu sesión de ejercicio en minutos:")) # Preguntamos las variables una vez sabemos el deporte, para que si no está disponible no se pidan
                    weight = float(input("\nIntroduce tu peso: "))

                    data = json.load(met) # Cargamos el json en un diccionario
                    boxing = data["Boxeo"] # Logramos el valor del MET desde el diccionario

                    kcal = (boxing * 0.0175) * weight # Fórmula del MET (MET * 0.0175 * peso)
                    kcal_total = kcal * sport_time
                    result = round(kcal_total, 2) # Redondeamos a dos decimales

                print(f"\nTu gasto calórico ha sido de {result} kcal") # Imprimimos resultado

            else:
                print("Tu deporte no está disponible o no está bien escrito, prueba de nuevo")

        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON.")
        except Exception as e:
            print(f"Se ha producido un error: {e}")

        exit = str(input("Si quieres cerrar el programa, presiona la tecla \"2\". Si quieres continuar, presiona cualquier otra")) # Un método que se me ha ocurrido para poder salir usando la variable anterior condition
        
        if exit == "2":
            condition = False
        else: 
            continue

burned_calories() # Ejecutamos la función