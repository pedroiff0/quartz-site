import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def newton_raphson():
    # Solicitar entradas do usuário
    func_input = input("Digite a função (use 'x' como variável): ")
    precision = int(input("Precisão (casas decimais): "))
    max_iter = int(input("Número máximo de iterações: "))
    x0 = float(input("Valor inicial (x0): "))
    
    # Configurações iniciais
    x = sp.symbols('x')
    try:
        func_expr = sp.sympify(func_input)
    except sp.SympifyError:
        print("Erro na função. Use operadores válidos (ex: x**2 + sp.sin(x)).")
        return
    
    f = sp.lambdify(x, func_expr, modules=['numpy'])
    df = sp.lambdify(x, sp.diff(func_expr, x), modules=['numpy'])
    tol = 10 ** (-precision)
    roots = []
    
    # Iterações
    for i in range(max_iter):
        try:
            f_x0 = f(x0)
            df_x0 = df(x0)
        except:
            print("Erro ao avaliar a função ou derivada.")
            return
        
        if df_x0 == 0:
            print("Derivada zero. Método interrompido.")
            return
        


        x_new = x0 - f_x0 / df_x0
        roots.append(x_new)
        
        print(f"Iteração {i+1}: x = {x_new:.{precision}f}")
        print(f"f(x): ", f_x0)
        print(f"f'(x): ", df_x0)
        print(f"x: ", x0)

        if abs(x_new - x0) < tol:
            print(f"Convergência em {i+1} iterações. Raiz: {x_new:.{precision}f}")
            break
        x0 = x_new
    else:
        print(f"Máximo de iterações atingido. Raiz aproximada: {x0:.{precision}f}")
    
    # Plotagem
    x_vals = np.linspace(min(roots) - 2, max(roots) + 2, 400)
    y_vals = f(x_vals)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.plot(x_new, f(x_new), 'ro', label='Raiz')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.title(f'Gráfico de f(x) = {func_expr}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

newton_raphson()