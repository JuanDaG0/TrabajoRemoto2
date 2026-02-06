"""
Calculadora de Salud - Equipo
"""

def calcular_imc(peso, altura):
    imc = peso / (altura * altura) 
    return imc
    
def calcular_grasa_corporal(peso, altura, edad, genero):
    """Calcula La Grasa Corporal"""
    imc = calcular_imc(peso, altura)
    if genero == "M":
        valor_genero = 10.8
    else:
        valor_genero = 0
    grasa = (1.2 * imc) + (0.23 * edad) - 5.4 - valor_genero
    return grasa

def calcular_tmb(peso, altura, edad, sexo):
    """Calcula la tasa metabolica basal"""

    altura_cm = altura * 100

    tmb = (10 * peso) + (6.25 * altura_cm) - (5 * edad) + sexo

    return float(tmb) 
    
    


def calcular_calorias_adelgazar(tmb, actividad):
    """Calcula calorías diarias para adelgazar"""
    if actividad == "1":
        factor = 1.2
    elif actividad == "2":
        factor = 1.375
    else:
        factor = 1.55
    return tmb * factor - 500
    


def menu():
    print("===== CALCULADORA DE SALUD =====")
    print("1. Calcular IMC")
    print("2. Calcular Grasa Corporal")
    print("3. Calcular TMB")
    print("4. Calcular Calorias para Adelgazar")

    opcion = input("Elige una opcion, solo el numero: ")

    if opcion == "1":
        print("CALCULADORA DE IMC")
        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu altura en metros: "))

        imc = calcular_imc(peso, altura)
        print("Tu IMC es:", round(imc, 2))

        if imc < 18.5:
            print("Clasificación: Bajo peso")
        elif imc < 25:
            print("Clasificación: Peso normal")
        elif imc < 30:
            print("Clasificación: Sobrepeso")
        else:
            print("Clasificación: Obesidad")

    elif opcion == "2":
        print("\nCALCULADORA DE GRASA CORPORAL")
        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu altura en metros: "))
        edad = int(input("Ingresa tu edad: "))
        genero = input("Ingresa tu género (M/F): ").upper()
        grasa = calcular_grasa_corporal(peso, altura, edad, genero)
        print("Tu porcentaje de grasa corporal es:", round(grasa, 2), "%")

    elif opcion == "3":
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        edad = int(input("Edad: "))
        sexo = input("Sexo (M/F): ").upper()
        tmb = calcular_tmb(peso, altura, edad, sexo)
        print("Tu TMB es:", round(tmb, 2), "calorías")

    elif opcion == "4":
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        edad = int(input("Edad: "))
        sexo = input("Sexo (M/F): ").upper()
        tmb = calcular_tmb(peso, altura, edad, sexo)

        print("Nivel de actividad:")
        print("1. Baja")
        print("2. Media")
        print("3. Alta")
        actividad = input("Elige (1-3): ")

        calorias = calcular_calorias_adelgazar(tmb, actividad)
        print("Calorías diarias para adelgazar:", round(calorias, 2))

    else:
        print("Opción no válida")


menu()