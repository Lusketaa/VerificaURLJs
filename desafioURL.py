url = input()

if "https://" in url:
    resultado = "URL segura"
# TODO: Implemente a condição necessária para a verificação da URL:
elif "http://" in url:
    # TODO: Atribua para a variável resultado a mensagem adequada:
    resultado = "URL nao segura"
else:
    # TODO: Atribua para a variável resultado a mensagem adequada:
    resultado = "Formato invalido"

# Exibe o resultado
print(resultado)