import matplotlib.pyplot as plt

# Dados do gráfico
categorias = ['MORADIA', 'CONDOMINIO', 'SUPERMERCADO', 'ÁGUA', 'LUZ', 'GÁS', 'IPTU',
              'PLANO DE SAÚDE', 'SEGURO DE VIDA', 'INVESTIMENTOS', 'OUTRAS DESPESAS ESSENCIAIS']
valores = [1000, 1600, 400, 100, 300, 150, 80, 500, 150, 300, 500]

# Criar o gráfico de barras
plt.figure(figsize=(10, 5))
plt.bar(categorias, valores, color='lightblue')

# Personalizar o gráfico
plt.xticks(rotation=45, ha='right')
plt.ylabel('R$')
plt.title('Distribuição de Despesas')

# Mostrar o gráfico
plt.tight_layout()
plt.show()
