"""
Calculadora de Salud - Equipo
"""

def calcular_imc(peso, altura):
    imc = peso / (altura * altura) 
    return imc
    


def calcular_grasa_corporal(imc, edad):
    """Calcula el porcentaje de grasa corporal"""
    


def calcular_tmb(peso, altura, edad, sexo):
    """Calcula la tasa metabolica basal"""
    


def calcular_calorias_adelgazar(tmb, actividad):
    """Calcula calorias diarias para adelgazar"""
    


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
        print("Grasa corporal")

    elif opcion == "3":
        print("TMB")

    elif opcion == "4":
        print("Calorias para adelgazar")

    else:
        print("No valido")


menu()