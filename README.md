# Validador-de-Segurança-de-Senhas

Um projeto desenvolvido em Python com foco em segurança, expressões regulares, boas práticas e testes automatizados. Este sistema permite validar senhas inseridas via terminal, classificando sua força e sugerindo melhorias.

---

## Objetivos do Projeto

Este projeto faz parte do meu roadmap de estudos em Python e tem como objetivo:

- Aplicar conceitos de segurança e validação.
- Praticar uso de Expressões Regulares (Regex).
- Adotar boas práticas de modularização.
- Implementar testes automatizados com `unittest`.
- Simular uma ferramenta real de análise de senhas.

---

## Funcionalidades

- Entrada de senha via terminal.
- Validação de critérios de segurança:
  - Mínimo de 8 caracteres.
  - Pelo menos 1 letra maiúscula.
  - Pelo menos 1 letra minúscula.
  - Pelo menos 1 número.
  - Pelo menos 1 caractere especial.
- Classificação da força da senha:
  - Fraca / Média / Forte.
- Sugestões automáticas de melhoria para senhas fracas.
- (Opcional) Gerador de senha segura.

---

## Tecnologias Utilizadas

- Python 3.x
- Expressões Regulares (`re`)
- Tipagem estática opcional (type hinting)
- Modularização de código
- Boas práticas (PEP8)
- Testes com `unittest`

---

## Estrutura do Projeto

```
validador_senhas/
├── main.py              # Ponto de entrada do programa
├── validacao.py         # Lógica de validação de senha
├── utils.py             # Funções auxiliares
├── gerador.py           # (Opcional) Gerador de senhas fortes
└── tests/
    └── test_validacao.py  # Testes automatizados
```

---

## Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/Mardonylima/Validador-de-Seguranca-de-Senhas.git
```

2. Ative o ambiente virtual (recomendado) e instale as dependências (caso use `requirements.txt`).

3. Execute o programa:
```bash
python main.py
```

---

## Próximos Passos

- Adicionar testes para todas as funções de validação.
- Implementar `getpass` para ocultar senha digitada.
- Criar gerador de senhas seguras.
- Adicionar criptografia usando `hashlib`.
- Exportar relatório de senhas.

---

## Autor

Desenvolvido por **Mardony**  
Projeto educacional (Pessoal)
