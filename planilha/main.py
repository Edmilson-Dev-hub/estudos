import pandas as pd

tabela = pd.read_csv("lista_clientes.csv")

linhas_iniciais = len(tabela)
# valores duplicados 
tabela = tabela.drop_duplicates()
# valores vazios
tabela = tabela.dropna()

linhas_finais = len(tabela)

print("Linhas Iniciais:", linhas_iniciais, "Linhas Finais:", linhas_finais)

# exploração 
resumo = tabela.describe(include="all")
correlacoes = tabela.corr(numeric_only=True)

'''
salvar em uma planilha
'''
with pd.ExcelWriter("Resumo.xlsx") as arquivo:
    resumo.to_excel(arquivo, sheet_name= "resumo")
    correlacoes.to_excel(arquivo, sheet_name= "correlacao") 