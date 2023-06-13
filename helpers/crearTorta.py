import pandas as pd
import matplotlib.pyplot as plt

def calcularPromedioSalarioPorEdad(dataFrame,rangos,columnaInteres,columnaPromedio,nombreGragica):
    plt.figure()
    #crear una columna nueva por rangos de edad
    dataFrame['rangosEdad']=pd.cut(dataFrame[columnaInteres],bins=rangos)
    #Calcular el promedio de los salarios por edad
    salarioPorRango=dataFrame.groupby('rangosEdad')[columnaPromedio].sum()
    #Definir los datos a graficar
    salario=salarioPorRango.values
    rangosEdad=salarioPorRango.index

    plt.pie(salario,labels=rangosEdad, autopct='%1.1f%%')
    plt.title('SALARIO EL NOMBRE POR EDAD')
    plt.savefig(f'./assets/img/{nombreGragica}.png')

