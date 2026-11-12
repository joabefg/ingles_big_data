from flask import request, render_template, render_template_string
import pandas as pd

# Adicionar lógica para importar os dados do xlsx
def importar(arquivo):
    df = pd.DataFrame(arquivo)

    # Descreve a estrutura do arquivo
    print(df.describe())
    # Verificar quanntidade de linhas/colunas
    print(df.shape)
    # Verificar tipos
    print(df.dtypes)
    # info gerais
    df.info()

    # 1. Validações Valores Ausente (Missing Values)
    print(df.isnull().sum())
    # preencher valores ausentes
    """
    df['product_name'] = df['product_name'].fillna('Produto não informado')
    df['product_category'] = df['product_category'].fillna('Produto sem categoria')
    df['product_price'] = df['product_price'].fillna(0.0)
    """
    df = df.fillna({
        'product_name': 'Produto não informado',
        'product_category': 'Produto sem categoria',
        'product_price': 0.0
    })
    df = df.dropna(subset=['product_rating'])

    # excluir duplicados
    df = df.drop_duplicates()
    df = df.drop_duplicates(
        subset=['cpf'],
        keep='first'
    )
    # first: mantém o primeiro
    # last: mantém o último
    # False: apaga todos os duplicados

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

    # manter apenas o que começa com algo
    df['link_img'] = df['link_img'].str.startswith(
        ('http')
    )
    df['email'] = df['email'].str.contains(
        ('@')
    )
