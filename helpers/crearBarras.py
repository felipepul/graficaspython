import matplotlib.pyplot as plt

def graficarPromediosalarial(dataFrame,campoX,campoY,nombreGrafica):
    colores = ['green','red','blue']
    salarioPromedio=dataFrame.groupby(campoX)[campoY].mean()

    #Generar la grafica
    plt.bar(salarioPromedio.index,salarioPromedio,color=colores)
    plt.title(" PROMEDIO SALARIAL")
    plt.xlabel("cargos")
    plt.ylabel("Salario mensual")

    plt.savefig(f'./assets/img/{nombreGrafica}.png')