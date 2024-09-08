import matplotlib.pyplot as plt
import random

def simulacion_galton(num_bolas, num_clavijas):
    """
    Simula la Máquina de Galton y devuelve una lista con la posición final de cada bola.
    
    Parámetros:
    num_bolas (int): Número de bolas que caen a través de la máquina.
    num_clavijas (int): Número de clavijas en la máquina.
    
    Retorna:
    list: Lista con la posición final de cada bola.
    """
    posiciones = []
    for _ in range(num_bolas):
        posicion = 0
        for _ in range(num_clavijas):
            if random.random() < 0.5:
                posicion -= 1
            else:
                posicion += 1
        posiciones.append(posicion)
    return posiciones

def grafica_distribucion(posiciones):
    """
    Genera una gráfica de barras que muestra la distribución de las posiciones finales de las bolas.
    
    Parámetros:
    posiciones (list): Lista con la posición final de cada bola.
    """
    plt.hist(posiciones, bins=20, edgecolor='black')
    plt.xlabel('Posición final')
    plt.ylabel('Frecuencia')
    plt.title('Distribución normal de la Máquina de Galton')
    plt.show()

# Parámetros de la simulación
num_bolas = 1000
num_clavijas = 10

# Simula la Máquina de Galton
posiciones = simulacion_galton(num_bolas, num_clavijas)

# Genera la gráfica de distribución
grafica_distribucion(posiciones)