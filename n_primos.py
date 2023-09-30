def eh_primo(n):
    """
    Esta função verifica se um número é primo ou não.
    Um número primo é um número natural maior que 1 que tem apenas dois divisores positivos distintos: 1 e ele mesmo.
    """
    if n <= 1:  # Se o número for menor ou igual a 1, ele não é primo
        return False
    elif n <= 3:  # Se o número for até 3, ele é primo
        return True
    elif n % 2 == 0 or n % 3 == 0:  # Se o número for divisível por 2 ou 3, ele não é primo
        return False
    i = 5
    while i * i <= n:  # Verifica se o número é divisível por qualquer número até sua raiz quadrada
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Solicita ao usuário que insira um número
num = int(input("Digite um número: "))

# Usa a função para verificar se o número é primo e imprime o resultado
if eh_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")

#numeros primos fazem parte de um conjunto que de passagem, são divisivel por eles mesmo, muito utilizado na area de criptografia