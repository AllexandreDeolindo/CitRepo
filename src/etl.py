from pyspark.sql.functions import (to_date, month, year, col, split, when, sum as spark_sum)
from pyspark.sql.types import DoubleType

def carregar_dados(spark, caminho_csv):
    return spark.read.format("csv") \
        .option("header", True) \
        .option("inferSchema", True) \
        .option("sep", ",") \
        .load(caminho_csv)

def transformar_dados(df):
    #Drop colunas desnecessárias
    df = df.drop(col("Point"))

    #Converter a data para formato adequado
    df = df.withColumn("date", to_date(col("Date"), "MMM yyyy")) \
        .withColumn("month", month(col("date"))) \
        .withColumn("year", year(col("date")))

    #Renomear colunas para snake_case
    for col_name in df.columns:
        df = df.withColumnRenamed(col_name, col_name.lower().replace(" ", "_"))

    #Criar tipo_de_fronteira (novo campo categórico)
    df = df.withColumn(
        "border_country",
        when(col("border") == "US-Canada Border", "Canada")
        .when(col("border") == "US-Mexico Border", "Mexico")
        .otherwise("Other")
    )

    #Categorizar tipos de entrada (ex: passageiro, veículo, carga)
    df = df.withColumn(
        "vehicle_category",
        when(col("measure").contains("Passenger"), "Passenger")
        .when(col("measure").contains("Vehicle"), "Vehicle")
        .when(col("measure").contains("Container"), "Load")
        .when(col("measure").contains("Truck"), "Load")
        .otherwise("Other")
    )

    #Garantir que latitude e longitude estejam como Double
    df = df.withColumn("value", col("value").cast(DoubleType())) \
            .withColumn("latitude", col("latitude").cast(DoubleType())) \
           .withColumn("longitude", col("longitude").cast(DoubleType()))

    #Agregar total por port/state/year/month
    df_agg = df.groupBy("port_name",
                        "state",
                        "year",
                        "month",
                        "vehicle_category") \
               .agg(spark_sum("value").alias("total_value"))

    return df_agg

def salvar_em_parquet(df, caminho_saida):
    df.write.mode("overwrite").parquet(caminho_saida)
