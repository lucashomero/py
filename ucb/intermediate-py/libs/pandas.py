# =====================================================
# PANDAS — RESUMO RÁPIDO
# =====================================================

# 1. IMPORTAÇÃO
import pandas as pd

# 2. CRIANDO DATAFRAMES E SERIES

# Series (coluna única)
s = pd.Series([10, 20, 30])
print(s)

# DataFrame (tabela)
dados = {
    "Nome": ["Lucas", "Ana", "João"],
    "Idade": [21, 22, 23],
    "Cidade": ["Brasília", "São Paulo", "Recife"]
}
df = pd.DataFrame(dados)
print(df)

# 3. LEITURA E ESCRITA DE ARQUIVOS

# CSV
df = pd.read_csv("arquivo.csv")
df.to_csv("saida.csv", index=False)

# Excel
# df = pd.read_excel("arquivo.xlsx")
# df.to_excel("saida.xlsx", index=False)

# 4. VISUALIZAÇÃO RÁPIDA

df.head()          # Primeiras 5 linhas
df.tail(3)         # Últimas 3 linhas
df.shape           # (linhas, colunas)
df.columns         # Nome das colunas
df.info()          # Resumo da estrutura
df.describe()      # Estatísticas básicas

# 5. ACESSO A DADOS

df["Nome"]             # Coluna única
df[["Nome", "Idade"]]  # Múltiplas colunas
df.iloc[0]             # Primeira linha (por posição)
df.loc[0]              # Primeira linha (por índice)
df.loc[0, "Nome"]      # Valor específico

# 6. FILTRAGEM DE DADOS

df[df["Idade"] > 21]                   # Linhas com idade > 21
df[df["Cidade"] == "Brasília"]        # Linhas com cidade específica

# 7. MODIFICAÇÃO DE DADOS

df["Idade"] = df["Idade"] + 1         # Atualiza coluna
df["NovaColuna"] = df["Idade"] * 2    # Cria nova coluna

# 8. AGRUPAMENTO E AGREGAÇÃO

df.groupby("Cidade")["Idade"].mean()   # Média da idade por cidade
df.groupby("Cidade").count()           # Contagem por cidade

# 9. ORDENAÇÃO

df.sort_values(by="Idade")             # Ordem crescente
df.sort_values(by="Idade", ascending=False)  # Ordem decrescente

# 10. VALORES NULOS

df.isnull()         # Verifica nulos (True/False)
df.isnull().sum()   # Conta nulos por coluna
df.dropna()         # Remove linhas com nulos
df.fillna(0)        # Substitui nulos por 0

# =====================================================
# FIM DO RESUMO DE PANDAS
# =====================================================
