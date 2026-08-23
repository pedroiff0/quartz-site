import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

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
y_values = [f_expr.evalf(subs={x: val}) for val in x_values]

# Verificando se y_values contém valores finitos
y_values = np.array(y_values, dtype=float)

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

# Exibindo os resultados da integral e volume do sólido de revolução
print(f"Função: f(x) = {func_input}")
print(f"Limites: [{a}, {b}]")
print(f"Volume do sólido de revolução: {volume}")

# Gráfico 3D do sólido girando
fig = plt.figure(figsize=(10, 5))
ax2 = fig.add_subplot(111, projection='3d')
theta = np.linspace(0, 2 * np.pi, 100)  # ângulo para a rotação

# Função para criar o sólido de revolução
def update(frame):
    ax2.cla()  # Limpa o gráfico anterior
    ax2.set_title('Sólido de Revolução Girando')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')

    # Cálculo das coordenadas do sólido girando em torno do eixo X
    X = np.outer(np.ones_like(theta), x_values)
    Y = np.outer(np.cos(theta), y_values)  # Rotaciona em torno do eixo Y
    Z = np.outer(np.sin(theta), y_values)

    # Plota o sólido
    ax2.plot_surface(X, Y, Z, color='lightgreen', alpha=0.7)

# Criando a animação
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=100)

plt.tight_layout()
plt.show()