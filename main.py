"""
Calculadora de Salud - Equipo
"""

def calcular_imc(peso, altura):
    """Calcula el indice de masa corporal"""
    


def calcular_grasa_corporal(imc, edad):
    """Calcula el porcentaje de grasa corporal"""
    


def calcular_tmb(peso, altura, edad, sexo):
    """Calcula la tasa metabolica basal"""

    altura_cm = altura * 100

    tmb = (10 * peso) + (6.25 * altura_cm) - (5 * edad) + sexo

    return float(tmb) 
    
    


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
        print("IMC")

    elif opcion == "2":
        print("Grasa corporal")

    elif opcion == "3":
        print("TMB")

    elif opcion == "4":
        print("Calorias para adelgazar")

    else:
        print("No valido")


menu()