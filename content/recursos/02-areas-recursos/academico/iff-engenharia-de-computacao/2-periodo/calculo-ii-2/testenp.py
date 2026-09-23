import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def newton_method(func_expr, var, x0, tol=1e-15, max_iter=100, decimal_places=50):
    # Converte a expressão simbólica em uma função numérica
    func = sp.lambdify(var, func_expr, 'numpy')
    dfunc = sp.lambdify(var, sp.diff(func_expr), 'numpy')  # Derivada da função

    x = x0
    errors = []  # Lista para armazenar os erros
    previous_root = None

    print(f"{'Iteração':<10} {'f(x)':<20} {'f\'(x)':<20} {'Raiz':<20}")
    print("-" * 70)

    for i in range(max_iter):
        fx = func(x)
        dfx = dfunc(x)
        
        if dfx == 0:  # Evita divisão por zero
            print("Derivada é zero. O método não pode continuar.")
            return None, errors
        
        x_new = x - fx / dfx
        
        # Calcula o erro e armazena
        error = abs(x_new - x)
        errors.append(error)

        # Exibe informações da interação
        print(f"{i+1:<10} {fx:<20.{decimal_places}} {dfx:<20.{decimal_places}} {x_new:<20.{decimal_places}}")

        # Verifica se a raiz está estável nas casas decimais desejadas
        if previous_root is not None:
            if round(x_new, decimal_places) == round(previous_root, decimal_places):
                print(f"Raiz encontrada: {x_new:.{decimal_places}f} após {i+1} iterações.")
                return x_new, errors
        
        previous_root = x_new
        
        if error < tol:
            print(f"Raiz encontrada: {x_new:.{decimal_places}f} após {i+1} iterações.")
            return x_new, errors
        
        x = x_new
    
    print("O método não convergiu.")
    return None, errors

def plot_function_and_derivative(func_expr, var, root, errors, tol, decimal_places):
    # Cria um intervalo para o gráfico
    x_vals = np.linspace(-3, 3, 400)
    func = sp.lambdify(var, func_expr, 'numpy')
    dfunc = sp.lambdify(var, sp.diff(func_expr), 'numpy')
    
    y_vals = func(x_vals)
    dy_vals = dfunc(x_vals)

    plt.figure(figsize=(12, 6))
    
    # Plotando f(x)
    plt.subplot(1, 2, 1)
    plt.plot(x_vals, y_vals, label=f'f(x) = {func_expr}', color='blue')
    
    # Plotando f'(x)
    plt.plot(x_vals, dy_vals, label=f"f'(x)", color='orange', linestyle='--')
    
    # Marcando a raiz encontrada
    if root is not None:
        plt.plot(root, func(root), 'ro')  # Raiz aproximada em vermelho
        plt.annotate(f'Raiz: {root:.{decimal_places}f}', (root, func(root)), textcoords="offset points", xytext=(0,10), ha='center')

    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    
    plt.title('Função e Derivada')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.legend()

    # Plotando o erro
    plt.subplot(1, 2, 2)
    
    error_vals = [abs(e) for e in errors]  # Usar os erros armazenados

    plt.plot(error_vals, label='Erro Absoluto', color='red', linestyle='--')
    
    # Adicionando linha de tolerância
    plt.axhline(y=tol, color='green', linestyle=':', label='Tolerância Máxima')

    if error_vals:
        max_error = max(error_vals)
        decimal_places_error = 2
        plt.annotate(f'Máx Erro: {max_error:{decimal_places_error}e}', xy=(len(error_vals)-1, max_error), 
                     textcoords="offset points", xytext=(0,-15), ha='center', color='black')

    plt.yscale('log')  # Escala logarítmica para melhor visualização do erro
    plt.title('Erro ao Longo das Iterações')
    plt.xlabel('Iteração')
    plt.ylabel('Erro Absoluto (Escala Log)')
    
    plt.grid()
    plt.legend()
    
    plt.tight_layout()
    
    plt.show()

def main():
    # Definindo a variável simbólica
    var = sp.symbols('x')

    # Entrada do usuário para a função e parâmetros
    func_input = input("Digite a função f(x) em termos de x (ex: x**2 - 2): ")
    tol_input = input("Digite a tolerância máxima (erro admitido): ")
    max_iter_input = input("Digite o número máximo de iterações: ")
    
    try:
        tol = float(tol_input)
        max_iter = int(max_iter_input)

        # Entrada do usuário para casas decimais
        decimal_places_input = input("Digite o número de casas decimais para exibir a raiz: ")
        decimal_places = int(decimal_places_input)

        # Chute inicial
        x0_input = input("Digite um chute inicial (x0): ")
        x0 = float(x0_input)

        # Convertendo a entrada do usuário para expressão simbólica
        func_expr = sp.sympify(func_input)

        # Calculando a raiz e capturando os erros
        root, errors = newton_method(func_expr, var, x0, tol=tol, max_iter=max_iter, decimal_places=decimal_places)

        # Plotando a função e sua derivada com erro
        plot_function_and_derivative(func_expr, var, root, errors, tol=tol, decimal_places=decimal_places)

    except Exception as e:
        print(f"Erro: {e}")

# Executar a função principal
if __name__ == "__main__":
    main()