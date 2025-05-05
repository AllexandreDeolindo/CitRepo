from pyspark.sql import SparkSession
from etl import carregar_dados, transformar_dados, salvar_em_parquet
from sql_queries import *

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("BorderCrossing") \
        .master("local") \
        .getOrCreate()

    caminho_csv = "C:/Users/allexandredeolindo/Documents/Learning/PlanoEstudo/ProjetoCIT/data/raw/Border_Crossing_Entry_Data.csv"
    caminho_parquet = "C:/Users/allexandredeolindo/Documents/Learning/PlanoEstudo/ProjetoCIT/data/output/output_final.parquet"

    df_raw = carregar_dados(spark, caminho_csv)
    df_raw.show(truncate = False)

    df_tratado = transformar_dados(df_raw)
    #salvar_em_parquet(df_tratado, caminho_parquet)
    df_tratado.show(truncate = False)

    df_tratado.createOrReplaceTempView("dados_fronteira")
    resultado = spark.sql(QUERY_TOP10_PORTOS)
    #resultado.show()

    spark.stop()