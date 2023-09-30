print("Piada mat discreta / uma mulher que ama matematica acaba de fazer ultrassom no hospital, logo ela vai ligar para seus pais para informa a noticia, quando informa seus pais, o pai logo pergunta :é menino ou menina?")

opcoes = ["SIM", "MENINO", "MENINA", "NÃO"]
resposta = input("Escolha uma opção: ")

if resposta in opcoes[:3]:
    print("Verdadeiro")
elif resposta == opcoes[3]:
    print("Falso")
else:
    print("Opção inválida. Por favor, escolha entre: " + ", ".join(opcoes))