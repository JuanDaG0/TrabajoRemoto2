"""
Calculadora de Salud - Equipo
"""

def calcular_imc(peso, altura):
    """Calcula el indice de masa corporal"""
    
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
    print("\nCALCULADORA DE GRASA CORPORAL")
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))
    edad = int(input("Ingresa tu edad: "))
    genero = input("Ingresa tu género (M/F): ").upper()
    grasa = calcular_grasa_corporal(peso, altura, edad, genero)
    print("Tu porcentaje de grasa corporal es:", round(grasa, 2), "%")

    elif opcion == "3":
        print("TMB")

    elif opcion == "4":
        print("Calorias para adelgazar")

    else:
        print("No valido")


menu()