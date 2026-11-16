# pip install sqlalchemy
from sqlalchemy import create_engine

def salvar_dados(dataframe):
    # 1. Preparar conexão
    engine_server = create_engine('mysql+mysqlconnector://root:1234@localhost:3306')

    # comando insert
    dataframe.to_sql(
        name='product',
        con=engine_server,
        if_exists='append',
        index=False,
        schema='inglesdb'
    )

