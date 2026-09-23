import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D
import ipywidgets as widgets
from IPython.display import display

# Definindo a função e os limites
func_input = 'sin(x)'  # Função a ser utilizada
a = 0  # Limite inferior
b = 1  # Limite superior

# Definindo a variável simbólica
x = sp.symbols('x')

# Convertendo a função de string para expressão simbólica
f_expr = sp.sympify(func_input)

# Calculando a integral da função no intervalo [a, b] para obter o volume do sólido de revolução
volume = sp.integrate(sp.pi * f_expr**2, (x, a, b)).evalf()

# Criando um array de valores dentro do intervalo
x_values = np.linspace(a, b, 100)
y_values = np.array([f_expr.evalf(subs={x: val}) for val in x_values], dtype=float)

# Exibindo os resultados da integral e volume do sólido de revolução
print(f"Função: f(x) = {func_input}")
print(f"Limites: [{a}, {b}]")
print(f"Volume do sólido de revolução: {volume}")

# Gráfico da função e área sob a curva
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label=f'f(x) = {func_input}', color='blue')
plt.fill_between(x_values, y_values, color='lightblue', alpha=0.5)
plt.title('Função e Área Sob a Curva')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.legend()
plt.grid()
plt.show()

# Gráfico 3D do sólido girando com controle interativo
fig = plt.figure(figsize=(10, 5))
ax2 = fig.add_subplot(111, projection='3d')
theta = np.linspace(0, 2 * np.pi, 100)  # ângulo para a rotação

# Slider para controlar o ângulo de rotação
angle_slider = widgets.FloatSlider(value=0, min=0, max=360, step=1, description='Ângulo (graus):')

def plot_solid(angle):
    ax2.cla()  # Limpa o gráfico anterior
    ax2.set_title('Sólido de Revolução Girando')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')

    # Cálculo das coordenadas do sólido girando em torno do eixo X
    X = np.outer(np.ones_like(theta), x_values)
    Y = np.outer(np.cos(np.radians(angle)), y_values)  # Rotaciona em torno do eixo Y baseado no ângulo
    Z = np.outer(np.sin(np.radians(angle)), y_values)

    # Plota o sólido
    ax2.plot_surface(X, Y, Z, color='lightgreen', alpha=0.7)

    # Adiciona seções transversais
    for i in range(len(x_values)):
        ax2.plot([x_values[i], x_values[i]], [0, y_values[i]], [0, 0], color='red', alpha=0.5)

# Usar widgets.interactive para atualizar o gráfico em tempo real com base no slider
widgets.interactive(plot_solid, angle=angle_slider)

# Exibir o slider e a animação juntos
display(angle_slider)