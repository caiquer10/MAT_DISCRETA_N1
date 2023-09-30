#CONCEITOS DE COMPARAÇÃO DA MAT DISCRETA
numero1 = float(input("Digite o PRIMEIRO número: "))
numero2 = float(input("Digite o SEGUNDO número: "))

# Compara os números e dá o valor do resultado
# A instrução if verifica se a condição (neste caso, num1 > num2) é verdadeira.
if numero1 > numero2:
    print(f"{numero1} é maior que {numero2}.")
elif numero1 < numero2:
    print(f"{numero1} é menor que {numero2}.")
else:
    print(f"{numero1} é igual a {numero2}.")