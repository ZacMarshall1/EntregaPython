import matplotlib.pyplot as plt

labels = ['MORADIA', 'CONDOMÍNIO', 'SUPERMERCADO', 'ÁGUA', 'LUZ', 'GÁS', 'IPTU',
              'PLANO DE SAÚDE', 'SEGURO DE VIDA', 'INVESTIMENTOS', 'OUTRAS DESPESAS ESSENCIAIS']
sizes = [1620, 270, 1080, 162, 270, 108, 108, 540, 162, 540, 540]

colors = ['gold', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink',
              'yellow', 'lightgrey', 'orange', 'lightblue', 'purple', 'red']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')

plt.title('Distribuição das Despesas Mensais')

plt.show()