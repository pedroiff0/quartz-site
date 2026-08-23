import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Função para calcular o raio da esfera
def sphere_radius(y):
    return np.sqrt(1 - y**2)  # Raio da esfera unitária

# Configurar a figura e o eixo 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Definir limites para y
y = np.linspace(-1, 1, 30)  # Aumentar o número de pontos para um espaçamento mais fino
spacing = 0.1  # Espaçamento entre as seções

# Criar seções transversais da esfera
for i in range(len(y)):
    radius = sphere_radius(y[i])
    theta = np.linspace(0, 2 * np.pi, 60)  # Ângulo para a seção circular
    x = radius * np.cos(theta)
    z = radius * np.sin(theta)
    
    # Adicionar um deslocamento no eixo Y para espaçar as seções
    ax.plot(x, y[i] + spacing * (i - len(y) // 2), z, color='b', alpha=0.7)

# Adicionar título e rótulos aos eixos
ax.set_title("Sólido de Revolução: Esfera com Espaçamento entre Seções")
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Definir proporção igual para melhor visualização
ax.set_box_aspect([1, 1, 1])  # Proporção igual

# Mostrar o gráfico
plt.show()