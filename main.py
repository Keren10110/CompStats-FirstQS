import csv
import os
import matplotlib.pyplot as plt
import numpy as np

# Path: main.py
# the file contains el sexo, la edad, el promedio final acumulado de la carrera, los ingresos estimados mensuales en dólares, si actualmente está trabajando o no, la altura en m
# el peso en kilogramos y estado civil con las categorías Soltero, Casado y Unión libre (Uni-lib)

#---------------------------------------------------------Funciones requeridads para realizar los cálculos -----------------------------------------------------

def read_file():
    with open(os.path.join(os.path.dirname(__file__), 'Egresados.csv'), newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        egresados = []
        for row in reader:
            egresados.append(row)
        # print(egresados)
        return egresados

def get_total_mujeres_trabajando(egresados):
    total_mujeres_trabajando = 0
    for egresado in egresados:
        if egresado['Sexo'].lower() == 'mujer' and egresado['Trabaja'].lower() == 'si':
            total_mujeres_trabajando += 1
    return total_mujeres_trabajando


def get_total_egresados_ganan_mas_95(egresados):
    total_egresados_ganan_mas_95 = 0
    for egresado in egresados:
        if float(egresado['Ingresos']) > 95:
            total_egresados_ganan_mas_95 += 1
    return total_egresados_ganan_mas_95

def get_total_egresados_obesos(egresados):
    total_egresados_obesos = 0
    for egresado in egresados:
        peso = 0
        altura = 0
        try:
            peso = float(egresado['Peso'].replace(',', '.'))
        except:
            peso = float(egresado['Peso'])

        try:
            altura = float(egresado['Altura'].replace(',', '.'))
        except:
            altura = float(egresado['Altura'])
        imc = peso / (altura ** 2)
        if imc >= 25 and imc < 30:
            total_egresados_obesos += 1
    return total_egresados_obesos

def get_ingresos_range(egresados):
    ingresos_range = []
    for egresado in egresados:
        ingresos_range.append(float(egresado['Ingresos']))
    return min(ingresos_range), max(ingresos_range)

def get_percentage_egresados_trabajando(egresados):
    total_egresados = len(egresados)
    total_egresados_trabajando = 0
    for egresado in egresados:
        if egresado['Trabaja'].lower() == 'si':
            total_egresados_trabajando += 1
    percentage_egresados_trabajando = (
        total_egresados_trabajando / total_egresados) * 100
    return percentage_egresados_trabajando

def get_coeficiente_asimetria_notas_promedio(egresados):
    promedios = []
    for egresado in egresados:
        try:
            promedio = float(egresado['Promedio'].replace(',', '.'))
        except:
            promedio = float(egresado['Promedio'])
        promedios.append(promedio)
    promedios.sort()
    n = len(promedios)
    promedio_medio = promedios[n // 2]
    promedio_medio_inferior = promedios[(n - 1) // 2]
    promedio_medio_superior = promedios[(n + 1) // 2]
    print(promedio_medio, promedio_medio_inferior, promedio_medio_superior)
    coeficiente_asimetria = (promedio_medio - promedio_medio_inferior) / \
        (promedio_medio_superior - promedio_medio_inferior)
    return coeficiente_asimetria

def get_curtosis_ingresos(egresados):
    ingresos = []
    for egresado in egresados:
        ingresos.append(float(egresado['Ingresos']))
    n = len(ingresos)
    ingresos.sort()
    ingresos_promedio = sum(ingresos) / n
    ingresos_desviacion_estandar = 0
    for ingreso in ingresos:
        ingresos_desviacion_estandar += (ingreso - ingresos_promedio) ** 2
    ingresos_desviacion_estandar = (
        ingresos_desviacion_estandar / (n-1)) ** 0.5
    curtosis = 0
    for ingreso in ingresos:
        curtosis += ((ingreso - ingresos_promedio) /
                     ingresos_desviacion_estandar) ** 4
    curtosis = (curtosis / n) - 3
    return curtosis

def get_coeficiente_variacion_edad(egresados):
    edades = []
    for egresado in egresados:
        edades.append(float(egresado['Edad']))
    n = len(edades)
    edades_promedio = sum(edades) / n
    edades_desviacion_estandar = 0
    for edad in edades:
        edades_desviacion_estandar += (edad - edades_promedio) ** 2
    edades_desviacion_estandar = (edades_desviacion_estandar / (n-1)) ** 0.5
    coeficiente_variacion = (
        edades_desviacion_estandar / edades_promedio) * 100
    return coeficiente_variacion


def get_height_average(egresados):
    heights = []
    for egresado in egresados:
        try:
            altura = float(egresado['Altura'].replace(',', '.'))
        except:
            altura = float(egresado['Altura'])
        heights.append(altura)
    height_average = sum(heights) / len(heights)
    return height_average

# get El cuartil que deja por debajo de la distribución el 50% de los pesos en  kg


def get_cuartil_peso(egresados):
    pesos = []
    for egresado in egresados:
        try:
            peso = float(egresado['Peso'].replace(',', '.'))
        except:
            peso = float(egresado['Peso'])
        pesos.append(peso)
    pesos.sort()
    cuartil_peso = pesos[len(pesos) // 2]
    return cuartil_peso

# get El cuartil que deja por debajo de la distribución el 25% de los ingresos.

def get_cuartil_ingresos(egresados):
    ingresos = []
    for egresado in egresados:
        try:
            ingreso = float(egresado['Ingresos'].replace(',', '.'))
        except:
            ingreso = float(egresado['Ingresos'])
        ingresos.append(ingreso)
    ingresos.sort()
    cuartil_ingresos = ingresos[len(ingresos) // 4]
    return cuartil_ingresos

# get El percentil 75 de las edades.

def get_percentil_75_edades(egresados):
    edades = []
    for egresado in egresados:
        edades.append(float(egresado['Edad']))
    edades.sort()
    percentil_75_edades = edades[(len(edades) * 3) // 4]
    return percentil_75_edades

def get_varianza_ingresos(egresados):
    ingresos = []
    for egresado in egresados:
        try:
            ingreso = float(egresado['Ingresos'].replace(',', '.'))
        except:
            ingreso = float(egresado['Ingresos'])
        ingresos.append(ingreso)
    std_ingresos = np.std(ingresos, ddof=1)
    varianza = std_ingresos**2
#########################GRAFICA DE LA DESVIACION ESTANDAR####################
# # # # # # # # # # # #     std_dev = np.std(ingresos)
# # # # # # # # # # # #     # Create a histogram of the data
# # # # # # # # # # # #     plt.hist(ingresos, bins=20, alpha=0.5, color='b', label='Data')
# # # # # # # # # # # #     # Add a vertical line representing the standard deviation
# # # # # # # # # # # #     plt.axvline(std_dev, color='r', linestyle='dashed', linewidth=2,
# # # # # # # # # # # #                 label=f'Standard Deviation: {std_dev:.2f}')

# # # # # # # # # # # #     # Add labels and a legend
# # # # # # # # # # # #     plt.xlabel('Value')
# # # # # # # # # # # #     plt.ylabel('Frequency')
# # # # # # # # # # # #     plt.legend(loc='upper right')

# # # # # # # # # # # # # Show the plot
# # # # # # # # # # # #     plt.show()


#########################GRAFICA DE LA VARIANZA####################
# # # # # # # # # # # #     # get the variance of the data set and plot it
# # # # # # # # # # # #     varianza = np.var(ingresos)
# # # # # # # # # # # #     plt.hist(ingresos, bins=20, alpha=0.5, color='b', label='Data')
# # # # # # # # # # # #     # Add a vertical line representing the standard deviation
# # # # # # # # # # # #     plt.axvline(varianza, color='r', linestyle='dashed', linewidth=2,
# # # # # # # # # # # #                 label=f'Variance: {varianza:.2f}')
# # # # # # # # # # # #     plt.xlabel('Value')
# # # # # # # # # # # #     plt.ylabel('Frequency')
# # # # # # # # # # # #     plt.legend(loc='upper right')
# # # # # # # # # # # #     plt.show()
    # varianza = std_dev ** 2

    return varianza

def get_desviacion_tipica_edades(egresados):
    edades = []
    for egresado in egresados:
        edades.append(float(egresado['Edad']))

    edades_desviacion_estandar = np.std(edades, ddof=1)

    # plt.plot(edades)

    return edades_desviacion_estandar


def get_percentil_85_ingresos(egresados):
    ingresos = []
    for egresado in egresados:
        try:
            ingreso = float(egresado['Ingresos'].replace(',', '.'))
        except:
            ingreso = float(egresado['Ingresos'])
        ingresos.append(ingreso)
    ingresos.sort()
    percentil_85_ingresos = ingresos[(len(ingresos) * 85) // 100]
    return percentil_85_ingresos


def get_percentage_egresados_casados(egresados):
    total_egresados = len(egresados)
    total_egresados_casados = 0
    for egresado in egresados:
        if egresado['Civil'].lower() == 'casado':
            total_egresados_casados += 1
    percentage_egresados_casados = (
        total_egresados_casados / total_egresados) * 100
    return percentage_egresados_casados

def get_percentage_egresados_solteros_trabajando(egresados):
    total_egresados = len(egresados)
    total_egresados_solteros_trabajando = 0
    for egresado in egresados:
        if egresado['Civil'].lower() == 'soltero' and egresado['Trabaja'].lower() == 'si':
            total_egresados_solteros_trabajando += 1
    percentage_egresados_solteros_trabajando = (
        total_egresados_solteros_trabajando / total_egresados) * 100
    return percentage_egresados_solteros_trabajando

#--------------------------------------------------------- Función principal ----------------------------------------------------------------
def main():
    egresados = read_file()
    print('Total de egresados: ', len(egresados))

    total_mujeres_trabajando = get_total_mujeres_trabajando(egresados)
    print('Total de mujeres trabajando: ', total_mujeres_trabajando)

    total_egresados_ganan_mas_95 = get_total_egresados_ganan_mas_95(egresados)
    print('Total de egresados que ganan más de 95 dólares: ',
          total_egresados_ganan_mas_95)
    
    total_egresados_obesos = get_total_egresados_obesos(egresados)
    print('Total de egresados obesos: ', total_egresados_obesos)

    ingresos_range = get_ingresos_range(egresados)
    print('Rango de ingresos: ', ingresos_range)

    percentage_egresados_trabajando = get_percentage_egresados_trabajando(
        egresados)
    print('Porcentaje de egresados trabajando: ',
          percentage_egresados_trabajando)
    
    try:
        coeficiente_asimetria_notas_promedio = get_coeficiente_asimetria_notas_promedio(
            egresados)
    except:
        print('Mappeado a 0 por arimethic overflow error')
        coeficiente_asimetria_notas_promedio = 0

    print('Coeficiente de asimetría para las notas promedio: ',
          coeficiente_asimetria_notas_promedio)
    
    curtosis_ingresos = get_curtosis_ingresos(egresados)
    print('Curtosis de los ingresos: ', curtosis_ingresos)

    coeficiente_variacion_edad = get_coeficiente_variacion_edad(egresados)
    print('Coeficiente de variación de la edad: ',
          coeficiente_variacion_edad)
    
    height_average = get_height_average(egresados)
    print('Promedio de altura: ', height_average)

    cuartil_peso = get_cuartil_peso(egresados)
    print('Cuartil de peso: ', cuartil_peso)

    cuartil_ingresos = get_cuartil_ingresos(egresados)
    print('Cuartil de ingresos: ', cuartil_ingresos)

    percentil_75_edades = get_percentil_75_edades(egresados)
    print('Percentil 75 de las edades: ', percentil_75_edades)

    variance_ingresos = get_varianza_ingresos(egresados)
    print('Varianza de los ingresos: ', variance_ingresos)

    desviacion_tipica_edades = get_desviacion_tipica_edades(egresados)
    print('Desviación típica de las edades: ', desviacion_tipica_edades)

    percentil_85_ingresos = get_percentil_85_ingresos(egresados)
    print('Percentil 85 de los ingresos: ', percentil_85_ingresos)

    percentage_egresados_casados = get_percentage_egresados_casados(egresados)
    print('Porcentaje de egresados casados: ', percentage_egresados_casados)

    percentage_egresados_solteros_trabajando = get_percentage_egresados_solteros_trabajando(
        egresados)
    print('Porcentaje de egresados solteros trabajando: ',
          percentage_egresados_solteros_trabajando)


main()
