# Função para validar o usuário
def validar_usuario(senha, usuario):
    # Definindo o usuário e senha corretos
    usuario_correto = "marcos123"
    senha_correta = "1234"

    # Verificando se o usuário e senha fornecidos são corretos
    if usuario == usuario_correto and senha == senha_correta:
        # Se o usuário e a senha estiverem corretos, conceda acesso
        return "Acesso concedido"
    else:
        # Se o usuário ou a senha estiverem incorretos, negue o acesso
        return "Acesso negado"

# Testando a função com o usuário e senha corretos
print(validar_usuario("1234", "marcos123"))
