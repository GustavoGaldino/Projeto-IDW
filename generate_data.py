import pandas as pd
import random
from faker import Faker
import csv

# Gerar um gerador de dados falso, para gerar um email aleatorio
fake = Faker()

# Tabela de Dimensão de Tempo (CSV)
datas = pd.date_range(start='2023-01-01', end='2023-11-09', freq='D')
tempo_df = pd.DataFrame({
    'Data': datas,
    'Dia_da_Semana': datas.day_name(),
    'Mes': datas.month_name(),
    'Ano': datas.year
})
tempo_df.to_csv('Tempo.csv', index=False)

# Tabela de Dimensão de Produto (CSV)
produtos = ['Celular', 'Notebook', 'Televisão', 'Câmera', 'Relógio']
categorias = ['Eletrônicos', 'Informática', 'Entretenimento', 'Fotografia', 'Acessórios']
precos = [3200, 6180, 1700, 750, 175]
custos = [1254, 5550, 1127.5, 214, 42]

produto_df = pd.DataFrame({
    'ID_do_Produto': range(1, 6),
    'Nome_do_Produto': produtos,
    'Categoria': categorias,
    'Preco': precos,
    'Custo': custos
})
produto_df.to_csv('Produto.csv', index=False)

estados_brasil = ['Pernambuco', 'Ceará', 'Paraíba', 'Rio Grande do Norte', 'Sao Paulo', 'Rio de Janeiro', 'Rio Grande do Sul']

nomes = []

with open('grupos.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header_row = True
    for row in csvreader:
        if header_row:
            header_row = False
            continue
        first_column = True
        for field in row:
            if first_column:
                first_column = False
                continue
            if field != '':
                nomes.append(field)

# Tabela de Dimensão de Cliente (XLSX)
clientes = [random.choice(nomes) for _ in range(100)]
emails = [fake.email() for _ in range(100)]
estados = [random.choice(estados_brasil) for _ in range(100)]
idades = [random.randint(12, 80) for _ in range(100)]
cliente_df = pd.DataFrame({
    'ID_do_Cliente': range(1, 101),
    'Nome': clientes,
    'Email': emails,
    'Estado': estados,
    'Idade': idades
})
cliente_df.to_excel('Cliente.xlsx', index=False)

# As duas funções seguintes geram ids aleatórios, com uma chance baixa
# de gerar um id nulo propositalmente, para forçar a etapa de limpeza de dados
def gerar_id_cliente():
    id = random.randint(-1,100)
    if id == 0 or id == -1:
        return None
    else:
        return id
    
def gerar_id_produto():
    if random.randint(0,50) == 0:
        return None
    else:
        return random.randint(1,5)

# Tabela de Fatos de Vendas (XLSX)
vendas_df = pd.DataFrame({
    'ID_da_Venda': range(1, 501),
    'ID_do_Produto': [ gerar_id_produto() for _ in range(500)],
    'ID_do_Cliente': [ gerar_id_cliente() for _ in range(500)],
    'Data': random.choices(datas, k=500),
    'Quantidade': [random.randint(1, 10) for _ in range(500)],
})

vendas_df.to_excel('Vendas.xlsx', index=False)
