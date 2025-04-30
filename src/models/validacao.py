import re
import random
import string

class Validacao:

    def __init__(self, tamanho_minimo=8):
        
        self.tamanho_minimo = tamanho_minimo

    def validar_criterios(self, senha: str) -> dict:

        resultados = {
            "tamanho_minimo": len(senha) >= 8,
            "maiuscula": bool(re.search(r'[A-Z]', senha)),
            "minuscula": bool(re.search(r'[a-z]', senha)),
            "numero": bool(re.search(r'\d', senha)),
            "especial": bool(re.search(r'[^a-zA-Z0-9]', senha))
        }

        return resultados

    def classificar_forca(self, senha: str) -> str:

        resultados = self.validar_criterios(senha)

        if not resultados["tamanho_minimo"]:
            return "Fraca"

        criterios_atingidos = sum(resultados.values())

        if criterios_atingidos == 5:
            return "Forte"

        elif criterios_atingidos >= 3:
            return "Média"

        else:
            return "Fraca"

    def gerar_senha_segura(self, tamanho: int = 12) -> str:
        # Retorna uma senha segura aleatória com base nos critérios

        # 1. Garante 1 caractere de cada tipo obrigatório
        maiuscula = random.choice(string.ascii_uppercase)
        minuscula = random.choice(string.ascii_lowercase)
        numero = random.choice(string.digits)
        especial = random.choice(string.punctuation)

        # 2. Preenche o restante da senha com caracteres mistos
        restante = tamanho - 4
        todos_os_caracteres = string.ascii_letters + string.digits + string.punctuation
        complemento = [random.choice(todos_os_caracteres) for _ in range(restante)]

        # 3. Embaralha tudo com random.shuffle
        senha_lista = list(maiuscula + minuscula + numero + especial) + complemento
        random.shuffle(senha_lista)
        senha_final = ''.join(senha_lista)

        # 4. Retorna a senha como string
        return senha_final