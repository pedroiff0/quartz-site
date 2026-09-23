import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def newton_raphson():
    # Solicitar a função, precisão e número máximo de iterações ao usuário
    func_input = input("Digite a função (em termos de x, use 'sin' e 'cos'): ")
    precision = int(input("Digite o número de casas decimais desejadas para a precisão: "))
    max_iterations = int(input("Digite o número máximo de iterações: "))
    x0 = float(input("Digite o valor inicial de x: "))
    
    # Definindo a variável simbólica
    x = sp.symbols('x')
    
    # Criar a função usando sympy
    try:
        func = sp.sympify(func_input)  # Converte a string da função em uma expressão simbólica
    except sp.SympifyError:
        print("Entrada inválida. Certifique-se de usar 'sin', 'cos', e operadores válidos.")
        return
    
    # Calcular a derivada da função
    func_deriv = sp.diff(func, x)  # Calcula a derivada da função

    # Funções para avaliação
    f = sp.lambdify(x, func)  # Cria uma função que pode ser chamada com valores numéricos
    df = sp.lambdify(x, func_deriv)  # Cria uma função para a derivada

    print("\nIniciando o Método de Newton...")
    print(f"Função: {func}")
    print(f"Derivada: {func_deriv}\n")

    # Listas para armazenar as iterações e raízes encontradas
    roots = []
    
    # Iterações do método de Newton
    for i in range(max_iterations):
        f_x0 = f(x0)
        df_x0 = df(x0)
        
        if df_x0 == 0:
            print("A derivada é zero. O método não pode continuar.")
            return
        
        x_new = x0 - (f_x0 / df_x0)
        
        # Exibir informações detalhadas da iteração
        print(f"Iteração {i+1}:")
        print(f"  x0 = {round(x0, precision)}")
        print(f"  f(x0) = {round(f_x0, precision)}")
        print(f"  f'(x0) = {round(df_x0, precision)}")
        print(f"  x_new = {round(x_new, precision)}\n")
        
        roots.append(x_new)  # Armazena a raiz encontrada
        
        # Verificar a condição de parada (precisão)
        if round(x_new, precision) == round(x0, precision):
            print(f"A raiz foi encontrada em {round(x_new, precision)} após {i+1} interações.")
            break
        
        x0 = x_new

    else:
        print(f"A raiz aproximada após {max_iterations} interações é {round(x0, precision)}.")

    # Visualização do gráfico
    plot_function_and_roots(func, roots)

def plot_function_and_roots(func, roots):
    # Gerar valores para o gráfico
    x_vals = np.linspace(-10, 10, 400)
    y_vals = [func.evalf(subs={sp.symbols('x'): val}) for val in x_vals]

    plt.figure(figsize=(10, 6))
    
    # Plotar a função
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    
    # Marcar as raízes encontradas
    for root in roots:
        plt.plot(root, func.evalf(subs={sp.symbols('x'): root}), 'ro')  # Raiz em vermelho
        plt.annotate(f'Raiz: {root:.2f}', xy=(root, func.evalf(subs={sp.symbols('x'): root})), 
                     textcoords="offset points", xytext=(0,10), ha='center', color='red')

    plt.axhline(0, color='black', lw=1)  # Linha horizontal em y=0
    plt.axvline(0, color='black', lw=1)  # Linha vertical em x=0
    
    plt.title('Gráfico da Função e Raízes Encontradas')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    
    plt.grid()
    
    # Ativar zoom interativo
    plt.gca().set_autoscale_on(True)
    
    plt.legend()
    
    plt.show()

# Chamar a função principal
newton_raphson()