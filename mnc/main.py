import math
from switch import Switch

# ----------------------------- MENU -----------------------------
def menu():
    print("\n1. Calculo determinante")
    print("2. Sistema triangular inferior")
    print("3. Sistema triangular superior")
    print("4. Decomponsição LU")
    print("5. Decomposição de Cholesky")
    print("6. Eliminação de Gauss Compacto")
    print("7. Eliminação de Gauss-Jordan")
    print("8. Método de Jacobi")
    print("9. Método de Gauss-Seidel")
    print("10. Calculo Matriz Inversa")
    print("11. Sair")
    print("-------------------------------------------------------------------------------------------")
    print("OBS: Utilize ',' para separar os elementos do vetor e ';' para separar as linhas da matriz")
    print("Exemplo de entrada de vetor: '2,-1,0'")
    print("Exemplo de entrada de matriz: '2.8,-1,0;1,2,-1;3,1,1'")
    print("-------------------------------------------------------------------------------------------")
    choice = input("Escolha um método: ")
    return choice

def main():
  while True:
    choice = menu()
    if choice == '11':
      break

    with Switch(choice) as case:
      # ----------------------------- CALCULO DETERMINANTE -----------------------------
      if case('1'): 
        ordem = int(input("Digite a ordem da matriz: "))
        matriz_input = input("Digite a matriz separada por virgula e uma nova linha separada por ponto-e-virgula: ")
        
        matriz = convert_to_float_matrix(matriz_input)
        print("Determinante: ", CalculoDeterminante(matriz))
        
      # ----------------------------- SISTEMA TRIANGULAR INFERIOR -----------------------------
      if case('2'): 
        ordem = int(input("Digite a ordem da matriz: "))
        vetor_input = input("Digite o vetor de termos independentes separado por virgula: ")
        matriz_input = input("Digite a matriz separada por virgula e uma nova linha separada por ponto-e-virgula: ")

        matriz = convert_to_float_matrix(matriz_input)
        termos_independentes = convert_to_float_list(vetor_input)
        print("Vetor solução: ", SistemaTriangularInferior(ordem, matriz, termos_independentes))
        
      # ----------------------------- SISTEMA TRIANGULAR SUPERIOR -----------------------------
      if case('3'):
        ordem = int(input("Digite a ordem da matriz: "))
        matriz_input = input("Digite a matriz separada por virgula e uma nova linha separada por ponto-e-virgula: ")
        vetor_input = input("Digite o vetor de termos independentes separado por virgula: ")

        matriz = convert_to_float_matrix(matriz_input)
        termos_independentes = convert_to_float_list(vetor_input)
        print("Vetor solução: ", SistemaTriangularSuperior(ordem, matriz, termos_independentes))
        
      # ----------------------------- DECOMPOSIÇÃO LU -----------------------------
      if case('4'):
        ordem = int(input("Digite a ordem da matriz: "))
        matriz_input = input("Digite a matriz separada por virgula e uma nova linha separada por ponto-e-virgula: ")
        vetor_input = input("Digite o vetor de termos independentes separado por virgula: ")

        matriz = convert_to_float_matrix(matriz_input)
        termos_independentes = convert_to_float_list(vetor_input)
        print("Vetor solução: ", DecomposicaoLU(ordem, matriz, termos_independentes))
      
      # ----------------------------- DECOMPOSIÇÃO DE CHOLESKY -----------------------------
      if case('5'):
        ordem = int(input("Digite a ordem da matriz: "))
        matriz_input = input("Digite a matriz separada por virgula e uma nova linha separada por ponto-e-virgula: ")
        vetor_input = input("Digite o vetor de termos independentes separado por virgula: ")

        matriz = convert_to_float_matrix(matriz_input)
        termos_independentes = convert_to_float_list(vetor_input)
        print("Vetor solução: ", Cholesky(ordem, matriz, termos_independentes))

      # ----------------------------- ELIMINAÇÃO DE GAUSS COMPACTO -----------------------------
      if case('6'):
        ordem = int(input("Digite a ordem da matriz: "))
        matriz_input = input("Digite a matriz separada por virgula e uma nova linha separada por ponto-e-virgula: ")
        vetor_input = input("Digite o vetor de termos independentes separado por virgula: ")

        matriz = convert_to_float_matrix(matriz_input)
        termos_independentes = convert_to_float_list(vetor_input)
        print("Vetor solução: ", GaussCompacto(ordem, matriz, termos_independentes))

      # ----------------------------- ELIMINAÇÃO DE GAUSS-JORDAN -----------------------------
      if case('7'):
        ordem = int(input("Digite a ordem da matriz: "))
        matriz_input = input("Digite a matriz separada por virgula e uma nova linha separada por ponto-e-virgula: ")
        vetor_input = input("Digite o vetor de termos independentes separado por virgula: ")

        matriz = convert_to_float_matrix(matriz_input)
        termos_independentes = convert_to_float_list(vetor_input)
        print("Vetor solução: ", GaussJordan(ordem, matriz, termos_independentes))
        
      # ----------------------------- JACOBI -----------------------------
      if case('8'):
        ordem = int(input("Digite a ordem da matriz: "))
        matriz_input = input("Digite a matriz separada por virgula e uma nova linha separada por ponto-e-virgula: ")
        vetor_input = input("Digite o vetor de termos independentes separado por virgula: ")
        aproximacao_input = input("Digite a aproximação inicial separada por virgula: ")
        precisao = float(input("Digite a precisão: "))
        max_iteracoes = int(input("Digite o número máximo de iterações: "))
        matriz = convert_to_float_matrix(matriz_input)
        termos_independentes = convert_to_float_list(vetor_input)
        aproximacao_inicial = convert_to_float_list(aproximacao_input)
        
        solucao, iteracoes = Jacobi(ordem, matriz, termos_independentes, aproximacao_inicial, precisao, max_iteracoes)
        print("Vetor solução: ", solucao)
        print("Número de iterações: ", iteracoes)
      # ----------------------------- GAUSS-SEIDEL -----------------------------
      if case('9'):
        ordem = int(input("Digite a ordem da matriz: "))
        matriz_input = input("Digite a matriz separada por virgula e uma nova linha separada por ponto-e-virgula: ")
        vetor_input = input("Digite o vetor de termos independentes separado por virgula: ")
        aproximacao_input = input("Digite a aproximação inicial separada por virgula: ")
        precisao = float(input("Digite a precisão: "))
        max_iteracoes = int(input("Digite o número máximo de iterações: "))
        matriz = convert_to_float_matrix(matriz_input)
        termos_independentes = convert_to_float_list(vetor_input)
        aproximacao_inicial = convert_to_float_list(aproximacao_input)
        
        solucao, iteracoes = GaussSeidel(ordem, matriz, termos_independentes, aproximacao_inicial, precisao, max_iteracoes)
        print("Vetor solução: ", solucao)
        print("Número de iterações: ", iteracoes)
        
      # ----------------------------- CALCULO MATRIZ INVERSA -----------------------------
      if case('10'):
        ordem = int(input("Digite a ordem da matriz: "))
        matriz_input = input("Digite a matriz separada por virgula e uma nova linha separada por ponto-e-virgula: ")
        matriz = convert_to_float_matrix(matriz_input)

        print("Matriz inversa: ", MatrizInversa(ordem, matriz))
      # ----------------------------- DEFAULT -----------------------------
      else:
        print("Opção inválida")

# ----------------------------- MÉTODOS -------------------------------------------#
#                                                                                  #
# ----------------------------- CALCULO MATRIZ INVERSA ----------------------------#
def MatrizInversa(ordem, matriz):
  determinante = CalculoDeterminante(matriz)
  
  if determinante == 0:
      print("A matriz não é inversível.")
  else:
      matriz_inversa = [[0] * ordem for _ in range(ordem)]
      for i in range(ordem):
          for j in range(ordem):
              sub_matriz = [row[:j] + row[j + 1:] for row in (matriz[:i] + matriz[i + 1:])]
              cofator = ((-1) ** (i + j)) * CalculoDeterminante(sub_matriz)
              matriz_inversa[j][i] = cofator / determinante
  
  return matriz_inversa
# ----------------------------- GAUSS-SEIDEL -----------------------------
def GaussSeidel(ordem, matriz, termos_independentes, aproximacao_inicial, precisao, max_iteracoes):
  x_atual = aproximacao_inicial[:]
  num_iteracoes = 0

  for _ in range(max_iteracoes):
      x_anterior = x_atual[:]
      for i in range(ordem):
          soma = sum(matriz[i][j] * x_atual[j] for j in range(ordem) if j != i)
          x_atual[i] = (termos_independentes[i] - soma) / matriz[i][i]
      
      if all(abs(x_atual[i] - x_anterior[i]) < precisao for i in range(ordem)):
          return x_atual, num_iteracoes

      num_iteracoes += 1

  return x_atual, num_iteracoes

# ----------------------------- JACOBI -----------------------------
def Jacobi(ordem, matriz, termos_independentes, aproximacao_inicial, precisao, max_iteracoes):
  x_atual = aproximacao_inicial[:]
  x_novo = [0.0] * ordem
  num_iteracoes = 0

  for _ in range(max_iteracoes):
      for i in range(ordem):
          soma = sum(matriz[i][j] * x_atual[j] for j in range(ordem) if j != i)
          x_novo[i] = (termos_independentes[i] - soma) / matriz[i][i]
      
      # Verifica a convergência
      if all(abs(x_novo[i] - x_atual[i]) < precisao for i in range(ordem)):
          return x_novo, num_iteracoes

      x_atual = x_novo[:]
      num_iteracoes += 1

  return x_novo, num_iteracoes
# ----------------------------- GAUSS-JORDAN -----------------------------
def GaussJordan(ordem, matriz, termos_independentes):
  matriz_aumentada = [matriz[i] + [termos_independentes[i]] for i in range(ordem)]
  
  for i in range(ordem):
      max_elem = abs(matriz_aumentada[i][i])
      max_row = i
      for k in range(i + 1, ordem):
          if abs(matriz_aumentada[k][i]) > max_elem:
              max_elem = abs(matriz_aumentada[k][i])
              max_row = k
      
      if max_row != i:
          matriz_aumentada[i], matriz_aumentada[max_row] = matriz_aumentada[max_row], matriz_aumentada[i]

      divisor = matriz_aumentada[i][i]
      for j in range(i, ordem + 1):
          matriz_aumentada[i][j] /= divisor

      for k in range(ordem):
          if k != i:
              factor = matriz_aumentada[k][i]
              for j in range(i, ordem + 1):
                  matriz_aumentada[k][j] -= factor * matriz_aumentada[i][j]

  solucao = [matriz_aumentada[i][ordem] for i in range(ordem)]
  
  return solucao

# ----------------------------- GAUSS COMPACTO -----------------------------
def GaussCompacto(ordem, matriz, termos_independentes):
  matriz_aumentada = [matriz[i] + [termos_independentes[i]] for i in range(ordem)]
  for i in range(ordem):
    max_elem = abs(matriz_aumentada[i][i])
    max_row = i
    for k in range(i + 1, ordem):
        if abs(matriz_aumentada[k][i]) > max_elem:
            max_elem = abs(matriz_aumentada[k][i])
            max_row = k
    
    if max_row != i:
        matriz_aumentada[i], matriz_aumentada[max_row] = matriz_aumentada[max_row], matriz_aumentada[i]

    for k in range(i + 1, ordem):
        factor = matriz_aumentada[k][i] / matriz_aumentada[i][i]
        for j in range(i, ordem + 1):
            matriz_aumentada[k][j] -= factor * matriz_aumentada[i][j]

  solucao = [0] * ordem

  for i in range(ordem - 1, -1, -1):
      solucao[i] = matriz_aumentada[i][ordem] / matriz_aumentada[i][i]
      for k in range(i - 1, -1, -1):
          matriz_aumentada[k][ordem] -= matriz_aumentada[k][i] * solucao[i]

  return solucao

# ----------------------------- CHOLESKY ---------------------------------
def Cholesky(ordem, matriz, termos_independentes):
  L = [[0.0] * ordem for _ in range(ordem)]

  for i in range(ordem):
      for j in range(i + 1):
          soma = sum(L[i][k] * L[j][k] for k in range(j))

          if i == j:
              L[i][j] = math.sqrt(matriz[i][i] - soma)
          else:
              L[i][j] = (matriz[i][j] - soma) / L[j][j]

          if L[i][j] == 0:
              raise ValueError("A matriz não é positiva definida.")
            
  def vetor_y(L, b):
    y = [0.0] * len(b)
    for i in range(len(b)):
        soma = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - soma) / L[i][i]
    return y

  def vetor_x(L_T, y):
    x = [0.0] * len(y)
    for i in range(len(y) - 1, -1, -1):
        soma = sum(L_T[i][j] * x[j] for j in range(i + 1, len(y)))
        x[i] = (y[i] - soma) / L_T[i][i]
    return x
  
  L_T = [[L[j][i] for j in range(ordem)] for i in range(ordem)]
  
  y = vetor_y(L, termos_independentes)  
  solucao = vetor_x(L_T, y)
  
  return solucao

# ----------------------------- DECOMPOSIÇÃO LU -----------------------------
def DecomposicaoLU(ordem, matriz, termos_independentes):
    L = [[0 for i in range(ordem)] for j in range(ordem)]
    U = [[0 for i in range(ordem)] for j in range(ordem)]
    
    for i in range(ordem):
      for k in range(i, ordem):
          soma = sum(L[i][j] * U[j][k] for j in range(i))
          U[i][k] = matriz[i][k] - soma

      for k in range(i, ordem):
          if i == k:
              L[i][i] = 1
          else:
              soma = sum(L[k][j] * U[j][i] for j in range(i))
              L[k][i] = (matriz[k][i] - soma) / U[i][i]
            
    def vetor_y(L, b):
      y = [0] * len(b)
      for i in range(len(b)):
          soma = sum(L[i][j] * y[j] for j in range(i))
          y[i] = (b[i] - soma) / L[i][i]
      return y
    
    def vetor_x(U, y):
      x = [0] * len(y)
      for i in range(len(y) - 1, -1, -1):
          soma = sum(U[i][j] * x[j] for j in range(i + 1, len(y)))
          x[i] = (y[i] - soma) / U[i][i]
      return x

    y = vetor_y(L, termos_independentes)
    solucao = vetor_x(U, y)
    
    return solucao

# ----------------------------- SISTEMA TRIANGULAR SUPERIOR -----------------------------
def SistemaTriangularSuperior(ordem, matriz, termos_independentes):
    solucao = [0] * ordem

    for i in range(ordem - 1, -1, -1):
        soma = 0
        for j in range(i + 1, ordem):
            soma += matriz[i][j] * solucao[j]
        solucao[i] = (termos_independentes[i] - soma) / matriz[i][i]
    
    return solucao

# ----------------------------- SISTEMA TRIANGULAR INFERIOR -----------------------------
def SistemaTriangularInferior(ordem, matriz, termos_independentes):
    solucao = [0] * ordem

    for i in range(ordem):
        soma = 0
        for j in range(i):
            soma += matriz[i][j] * solucao[j]
        solucao[i] = (termos_independentes[i] - soma) / matriz[i][i]
    
    return solucao

# ----------------------------- CALCULO DETERMINANTE -----------------------------
def CalculoDeterminante(matriz):
    ordem = len(matriz)

    if ordem == 1:
        return matriz[0][0]
    
    if ordem == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    def sub_matriz(matriz, linha, coluna):
        return [row[:coluna] + row[coluna + 1:] for row in (matriz[:linha] + matriz[linha + 1:])]
    
    determinante = 0
    for coluna in range(ordem):
        menor = sub_matriz(matriz, 0, coluna)
        cofator = ((-1) ** coluna) * matriz[0][coluna] * CalculoDeterminante(menor)
        determinante += cofator
    
    return determinante

# ----------------------------- UTILS -----------------------------
def convert_to_float_list(vetor):
    return [*map(float, vetor.split(','))]

def convert_to_float_matrix(matriz):
    return [[*map(float, linha.split(','))] for linha in matriz.split(';')]

# ----------------------------- MAIN -----------------------------
if __name__ == "__main__":
  main()
  