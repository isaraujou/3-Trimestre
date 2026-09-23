import pandas as pd

#1. lê a planilha do Excel
# Substitua ´dados_alunos.csv por o caminho do seu arquivo CSV
df = pd.read_csv('dados_aluno.csv')

# O pandas lê direto da nuvem!
tabela = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRY1RA6STvRwr8X9EspLuOh4_LCBmheuYMRMbrYonf3Jc8TTdRYC5xH0Zq87aRWyi9gck_SjJd83dgu/pub?output=csv')

# Mostra as primeiras linhas
print(tabela.head(5))