import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def plot_area_under_curve(ax, func, x_range):
    """Plota a área sob a curva."""
    x_vals = np.linspace(x_range[0], x_range[1], 100)
    y_vals = func(x_vals)

    ax.plot(x_vals, y_vals, label='f(x)', color='blue')
    ax.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
    ax.set_title('Área sob a Curva')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axhline(0, color='black', lw=0.5)
    ax.axvline(0, color='black', lw=0.5)
    ax.legend()

def plot_solid_of_revolution(ax, func, x_range):
    """Plota o sólido de revolução."""
    x_vals = np.linspace(x_range[0], x_range[1], 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    X, T = np.meshgrid(x_vals, theta)
    
    Y = func(X) * np.cos(T)
    Z = func(X) * np.sin(T)
    
    ax.plot_surface(X, Y, Z, color='cyan', alpha=0.6)
    ax.set_title('Sólido de Revolução')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

def animate_solid(func, x_range):
    """Anima o sólido de revolução girando em torno do eixo X."""
    
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    x_vals = np.linspace(x_range[0], x_range[1], 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    
    def update(frame):
        ax.clear()
        ax.set_xlim([x_range[0], x_range[1]])
        ax.set_ylim([-2, 2])
        ax.set_zlim([-2, 2])
        ax.set_title('Sólido de Revolução (Animação)')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
        Y = func(x_vals) * np.cos(theta + frame / 10.0)
        Z = func(x_vals) * np.sin(theta + frame / 10.0)
        
        ax.plot_surface(x_vals[:, None], Y.T, Z.T, color='lightcoral', alpha=0.6)

    ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)
    plt.show()

def plot_circular_sections(ax, func, x_range):
    """Plota as seções circulares no plano 2D."""
    x_vals = np.linspace(x_range[0], x_range[1], 10)
    y_vals = func(x_vals)

    for i in range(len(x_vals)):
        circle_x = y_vals[i] * np.cos(np.linspace(0, 2 * np.pi, 100))
        circle_y = y_vals[i] * np.sin(np.linspace(0, 2 * np.pi, 100))
        
        ax.plot(circle_x + x_vals[i], circle_y, color='red', alpha=0.3)

    ax.set_title('Seções Circulares no Sólido de Revolução')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_aspect('equal')

def main():
    print("Calculadora de Sólidos de Revolução")
    
    x = sp.symbols('x')
    func_input = input("Digite a função f(x) para integrar (ex: sqrt(sin(x)) + cos(x)**2): ")
    
    try:
        func_sympy = sp.sympify(func_input)
        func_np = sp.lambdify(x, func_sympy, 'numpy')
        derivative_func_sympy = sp.diff(func_sympy)
        integral_func_sympy = sp.integrate(func_sympy)
        
        print(f"\nFunção: f(x) = {func_sympy}")
        print(f"Derivada: f'(x) = {derivative_func_sympy}")
        print(f"Integral: ∫f(x) dx = {integral_func_sympy} + C")
        
    except sp.SympifyError as e:
        print(f"Erro na entrada da função: {e}")
        return

    lower_limit = float(input("Digite o limite inferior da integral: "))
    upper_limit = float(input("Digite o limite superior da integral: "))
    
    fig, axs = plt.subplots(1, 2, figsize=(14, 6), subplot_kw={0: {}, 1: {'projection': '3d'}})
    plot_area_under_curve(axs[0], func_np, (lower_limit, upper_limit))
    plot_solid_of_revolution(axs[1], func_np, (lower_limit, upper_limit))
    plt.show()

    animate_solid(func_np, (lower_limit, upper_limit))

    fig, ax = plt.subplots(figsize=(8, 8))
    plot_circular_sections(ax, func_np, (lower_limit, upper_limit))
    plt.show()

if __name__ == "__main__":
   main()
