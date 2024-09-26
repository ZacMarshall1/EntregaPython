import pandas as pd

# Dados das despesas
dados = {
    "Categoria": [
        "MORADIA",
        "CONDOMÍNIO",
        "SUPERMERCADO",
        "ÁGUA",
        "LUZ",
        "GÁS",
        "IPTU",
        "PLANO DE SAÚDE",
        "SEGURO DE VIDA",
        "INVESTIMENTOS",
        "OUTRAS DESPESAS ESSENCIAIS",
        "TOTAL"
    ],
    "Valor (R$)": [
        1620.00,
        270.00,
        1080.00,
        162.00,
        270.00,
        108.00,
        108.00,
        540.00,
        162.00,
        540.00,
        540.00,
        5400.00
    ]
}

# Criando o DataFrame
tabela_despesas = pd.DataFrame(dados)

# Exibindo a tabela
print(tabela_despesas)