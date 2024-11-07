# Explicação do Código
# Função calculate_factorial(n) :
# Esta função calcula o fatorial de um número n e imprime o valor atualizado a cada multiplicação.
# Entrada do Usuário :
# O código solicita ao usuário que insira um número inteiro.
# Verificação das Condições Especiais :
# Se o número for negativo, exibe uma mensagem informando que o fatorial não está definido para números negativos.
# Se o número for 0, exibe que 0!=1.
# Cálculo do Fatorial :
# O código chama a função calculate_factorial(num) e imprime o resultado final.


def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        print(f"Atualizando o valor: {factorial} (Multiplicando por {i})")
    return factorial

# Solicita ao usuário que entre com um número
num = int(input("Digite um número inteiro para calcular seu fatorial: "))

if num < 0:
    print("O fatorial não está definido para números negativos.")
elif num == 0:
    print("0! é igual a 1.")
else:
    # Calcula e explica o processo do fatorial
    result = calculate_factorial(num)
    print(f"\n{num}! (fatorial de {num}) é igual a: {result}")