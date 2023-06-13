from data.apartamentos import apartamento1, apartamento2
import pandas as pd
from helpers.crearTablasHTML import crearTablas
from helpers.crearBarras import graficarPromediosalarial
from helpers.crearTorta import calcularPromedioSalarioPorEdad

# 1. Crear el DATAFRAME

tabla1 = pd.DataFrame(apartamento1, columns=["Edades"])
tabla2 = pd.DataFrame(apartamento2, columns=["Edades"])
tabla3 = pd.read_csv("./data/empleados.csv")

# print(tabla1)
# print(tabla2)
# print(tabla3)
# Efectuando Filtros con python

# 1.Definir una condicion logica
empleadosJovenesAnalista1 = tabla3.query('cargo=="analista1"')
empleadosSalarioBajo = tabla3.query('salario<5000000 and cargo=="analista2"')
empleadosADespedir = tabla3.query("edad>=50")
# print(filtro)

# 2.creamos una tabla html con el dataframe del filtro
crearTablas(empleadosJovenesAnalista1, "tablaJovenes")
crearTablas(empleadosSalarioBajo, "tablabajossalarios")
crearTablas(empleadosADespedir, "oportunidadmejora")


# estadisticasAPTO1 = tabla1.describe()
# estadisticasAPTO2 = tabla2.describe()
# estadisticasEMPLEADOS = tabla3.describe()

# print(estadisticasAPTO1)
# print("\n")
# print(estadisticasAPTO2)
# print("\n")
# print(estadisticasEMPLEADOS)

#Genero graficas
graficarPromediosalarial(empleadosADespedir,'cargo','salario','graficajubilados')
calcularPromedioSalarioPorEdad(empleadosJovenesAnalista1,[20,30,40,50,60],'edad','salario','graficatortanalista1')
