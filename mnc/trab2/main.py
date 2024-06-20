import numpy as np
from switch import Switch

# ----------------------------- MENU -----------------------------
def menu():
    print("\n1. Interpolacão de Newton")
    print("2. Interpolação de Newton-Gregory")
    print("3. Coeficiente de determinação")
    print("4. Ajusta pontos tabelados a uma reta")
    print("5. Ajusta pontos tabelados a um polinômio de grau desejado")
    print("6. Ajusta pontos tabelados de um exponencial")
    print("7. Sair")
    print("-------------------------------------------------------------------------------------------")
    print("OBS: Utilize ',' para separar os elementos de vetor")
    print("Exemplo de entrada de vetor: '2,-1,0'")
    print("-------------------------------------------------------------------------------------------")
    choice = input("Escolha um método: ")
    return choice

def main():
  while True:
    choice = menu()
    if choice == '7':
      break

    with Switch(choice) as case:
      if case('1'): 
        num_pontos = int(input("Digite o número de pontos da tabela: "))
        xs = input("Digite os valores de x da tabela de valores separado por vírgula: ")
        ys = input("Digite os valores de y da tabela de valores separado por vírgula: ")
        x = float(input("Digite o valor de x que deseja calcular: "))
        
        vetor_x = convert_to_float_list(xs)
        vetor_y = convert_to_float_list(ys)  
        tabela = convert_to_table(vetor_x, vetor_y)
        
        valor_interpolado = interpolacao_newton(num_pontos, tabela, x)
        print("Valor do polinômio interpolado em x = {}: {}".format(x, valor_interpolado))

      if case('2'):
        num_pontos = int(input("Digite o número de pontos da tabela: "))
        xs = input("Digite os valores de x da tabela de valores separado por vírgula: ")
        ys = input("Digite os valores de y da tabela de valores separado por vírgula: ")
        x = float(input("Digite o valor de x que deseja calcular: "))
        
        vetor_x = convert_to_float_list(xs)
        vetor_y = convert_to_float_list(ys)  
        tabela = convert_to_table(vetor_x, vetor_y)

        valor_interpolado = interpolacao_newton_gregory(num_pontos, tabela, x)
        print("Valor do polinômio interpolado em x = {}: {}".format(x, valor_interpolado))
      
      if case('3'):
        num_pontos = int(input("Digite o número de pontos da tabela: "))
        xs = input("Digite os valores de x da tabela de valores separado por vírgula: ")
        ys = input("Digite os valores de y da tabela de valores separado por vírgula: ")
        
        vetor_x = convert_to_float_list(xs)
        vetor_y = convert_to_float_list(ys)  
        tabela = convert_to_table(vetor_x, vetor_y)

        r2 = coeficiente_determinacao(num_pontos, tabela)
        print("Coeficiente de determinação (R²):", r2)
      
      if case('4'):
        num_pontos = int(input("Digite o número de pontos da tabela: "))
        xs = input("Digite os valores de x da tabela de valores separado por vírgula: ")
        ys = input("Digite os valores de y da tabela de valores separado por vírgula: ")
        
        vetor_x = convert_to_float_list(xs)
        vetor_y = convert_to_float_list(ys)  
        tabela = convert_to_table(vetor_x, vetor_y)
        
        b, a, valores_ajustados, r2 = ajustar_reta(num_pontos, tabela)
        print("Coeficiente de grau 1 (a):", a)
        print("Termo independente (b):", b)
        print("Valores ajustados:", valores_ajustados)
        print("Coeficiente de determinação (R²):", r2)
        
      if case('5'):
        num_pontos = int(input("Digite o número de pontos da tabela: "))
        grau = int(input("Digite o grau do polinômio: "))
        xs = input("Digite os valores de x da tabela de valores separado por vírgula: ")
        ys = input("Digite os valores de y da tabela de valores separado por vírgula: ")
        
        vetor_x = convert_to_float_list(xs)
        vetor_y = convert_to_float_list(ys)  
        tabela = convert_to_table(vetor_x, vetor_y)
        
        coeficientes, valores_ajustados, r2 = ajustar_polinomio(num_pontos, grau, tabela)
        print("Coeficientes do polinômio ajustado:", coeficientes)
        print("Valores ajustados:", valores_ajustados)
        print("Coeficiente de determinação (R²):", r2)
      
      if case('6'):
        num_pontos = int(input("Digite o número de pontos da tabela: "))
        xs = input("Digite os valores de x da tabela de valores separado por vírgula: ")
        ys = input("Digite os valores de y da tabela de valores separado por vírgula: ")
        
        vetor_x = convert_to_float_list(xs)
        vetor_y = convert_to_float_list(ys)  
        tabela = convert_to_table(vetor_x, vetor_y)
        
        a, b, valores_ajustados, r2 = ajustar_curva_exponencial(num_pontos, tabela)
        print("Coeficiente 'a' da equação ajustada:", a)
        print("Coeficiente 'b' da equação ajustada:", b)
        print("Valores ajustados:", valores_ajustados)
        print("Coeficiente de determinação (R²):", r2)
      # ----------------------------- DEFAULT -----------------------------
      else:
        print("Opção inválida")

# ----------------------------- MÉTODOS -------------------------------------------#
#                                                                                  #
# ----------------------------- Interpolacão de Newton ----------------------------#
def interpolacao_newton(num_pontos, tabela, x):
    x_tabela = [ponto[0] for ponto in tabela]
    y_tabela = [ponto[1] for ponto in tabela]

    coeficientes = [0] * num_pontos
    coeficientes[0] = y_tabela[0]
    
    for j in range(1, num_pontos):
        for i in range(num_pontos - 1, j - 1, -1):
            y_tabela[i] = (y_tabela[i] - y_tabela[i - 1]) / (x_tabela[i] - x_tabela[i - j])
        coeficientes[j] = y_tabela[j]

    polinomio = coeficientes[-1]
    for i in range(num_pontos - 2, -1, -1):
        polinomio = polinomio * (x - x_tabela[i]) + coeficientes[i]

    return polinomio

# ----------------------------- Interpolacão de Newton-Gregory ----------------------------#
def interpolacao_newton_gregory(num_pontos, tabela, x):
    # Extrair x e y da tabela como floats
    x_tabela = [float(ponto[0]) for ponto in tabela]
    y_tabela = [float(ponto[1]) for ponto in tabela]

    # Construir a tabela de diferenças divididas
    diferencias_divididas = [y_tabela[:]]  # A primeira linha é y_tabela

    for i in range(1, num_pontos):
        linha = []
        for j in range(num_pontos - i):
            diff = (diferencias_divididas[i - 1][j + 1] - diferencias_divididas[i - 1][j]) / (x_tabela[j + i] - x_tabela[j])
            linha.append(diff)
        diferencias_divididas.append(linha)

    # Calcular o valor interpolado em x
    polinomio = y_tabela[0]
    termo = 1.0
    for i in range(1, num_pontos):
        termo *= (x - x_tabela[i - 1])
        polinomio += diferencias_divididas[i][0] * termo

    return polinomio

# ----------------------------- Coeficiente de determinação ----------------------------#
def coeficiente_determinacao(num_pontos, tabela):
    x_tabela = np.array([float(ponto[0]) for ponto in tabela])
    y_tabela = np.array([float(ponto[1]) for ponto in tabela])
    
    polinomio_coeficientes = np.polyfit(x_tabela, y_tabela, num_pontos-1)
    polinomio = np.poly1d(polinomio_coeficientes)
    
    y_ajustado = polinomio(x_tabela)
    
    ss_total = np.sum((y_tabela - np.mean(y_tabela))**2)
    ss_residual = np.sum((y_tabela - y_ajustado)**2)
    r_squared = 1 - (ss_residual / ss_total)
    
    return r_squared

# ----------------------------- Ajusta pontos tabelados a uma reta ----------------------------#
def ajustar_reta(num_pontos, tabela):
    if num_pontos != len(tabela):
        raise ValueError("O número de pontos não corresponde ao tamanho da tabela.")

    x_tabela = np.array([float(ponto[0]) for ponto in tabela])
    y_tabela = np.array([float(ponto[1]) for ponto in tabela])
    
    a1, a0 = np.polyfit(x_tabela, y_tabela, 1)
    
    y_ajustado = a0 + a1 * x_tabela
    
    ss_total = np.sum((y_tabela - np.mean(y_tabela))**2)
    ss_residual = np.sum((y_tabela - y_ajustado)**2)
    r_squared = 1 - (ss_residual / ss_total)
    
    return a0, a1, y_ajustado, r_squared

# ----------------------------- Ajusta pontos tabelados a um polinômio de grau desejado ----------------------------#
def ajustar_polinomio(num_pontos, grau, tabela):
    if num_pontos != len(tabela):
        raise ValueError("O número de pontos não corresponde ao tamanho da tabela.")
    
    if grau >= num_pontos:
        raise ValueError("O grau do polinômio deve ser menor que o número de pontos.")

    x_tabela = np.array([float(ponto[0]) for ponto in tabela])
    y_tabela = np.array([float(ponto[1]) for ponto in tabela])
    
    coeficientes = np.polyfit(x_tabela, y_tabela, grau)
    
    polinomio = np.poly1d(coeficientes)
    y_ajustado = polinomio(x_tabela)
    
    ss_total = np.sum((y_tabela - np.mean(y_tabela))**2)
    ss_residual = np.sum((y_tabela - y_ajustado)**2)
    r_squared = 1 - (ss_residual / ss_total)
    
    return coeficientes, y_ajustado, r_squared

# ----------------------------- Ajusta pontos tabelados de um exponencial ----------------------------#
def ajustar_curva_exponencial(num_pontos, tabela):
    if num_pontos != len(tabela):
        raise ValueError("O número de pontos não corresponde ao tamanho da tabela.")
    
    x_tabela = np.array([float(ponto[0]) for ponto in tabela])
    y_tabela = np.array([float(ponto[1]) for ponto in tabela])
    
    a, b = np.polyfit(x_tabela, np.log(y_tabela), 1, w=np.sqrt(y_tabela))
    
    y_ajustado = a + b * x_tabela
    y_ajustado = np.exp(y_ajustado)
    
    ss_total = np.sum((y_tabela - np.mean(y_tabela))**2)
    ss_residual = np.sum((y_tabela - y_ajustado)**2)
    r_squared = 1 - (ss_residual / ss_total)
    
    return np.exp(a), b, y_ajustado, r_squared

# ----------------------------- UTILS -----------------------------
def convert_to_float_list(vetor):
  return [*map(float, vetor.split(','))]

def convert_to_table(v1, v2):
  return list(zip(v1, v2))

# ----------------------------- MAIN -----------------------------
if __name__ == "__main__":
  main()
  