from flask import request, render_template, render_template_string
import pandas as pd

# Adicionar lógica para importar os dados do xlsx
def importar(arquivo):
    df = pd.read_csv(arquivo)
    # Descreve a estrutura do arquivo
    #print(df.describe())

    # 1. Validações Valores Ausente (Missing Values)
    print(df.isnull().sum())
    # preencher valores ausentes
    df = df.fillna({
        'product_name': 'Produto não informado',
        'product_category': 'Produto sem categoria',
        'product_price': 0.0
    })
    print(df.columns.tolist())
    df = df.dropna(subset=['product_ratings'])

    # excluir duplicados
    df = df.drop_duplicates()

    # padronizar
        # tirar espaços da frente/atrás
    df['product_name'] = df['product_name'].str.strip()
        # coloca tudo em minúsculo (upper para maíusculo)
    df['product_name'] = df['product_name'].str.lower()
        # coloca a primeira letra em maiúsculo (Capital)
    df['product_name'] = df['product_name'].str.title()

    # converter 'sete' = None
    df['product_price'] = pd.to_numeric(
        df['product_price'],
        errors='coerce'
    )

    print(df.head(10))
