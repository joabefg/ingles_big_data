# pip install sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

# 1. Preparar conexão
engine_server = create_engine('mysql+mysqlconnector://root:1234@localhost:3306')

def buscar_banco():
    conn = engine_server.connect()
    sql = "SELECT * FROM product"
    df = pd.read_sql(sql, con=conn)
    return df

def salvar_dados(dataframe):
    # comando insert
    dataframe.to_sql(
        name='product',
        con=engine_server,
        if_exists='append',
        index=False,
        schema='inglesdb'
    )



