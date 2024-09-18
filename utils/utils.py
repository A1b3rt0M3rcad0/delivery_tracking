# Função para gerar o código de entrega
def gerar_codigo_entrega():
    import random
    import string
    prefixo = "BR"
    sufixo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return f"{prefixo}-{sufixo}"