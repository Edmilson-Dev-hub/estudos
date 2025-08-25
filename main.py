import pandas as pd
import plotly.express as px

tabela = pd.read_csv("estudo_analise.csv")
print(tabela)

correlacao = tabela.corr(numeric_only=True)
print(correlacao)

grafico_correlacao = px.imshow(correlacao, text_auto=True, color_continuous_scale="Greens")
grafico_correlacao.show()

