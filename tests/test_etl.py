import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from src.etl import transformar_dados

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder \
        .appName("ETL Unit Test") \
        .master("local[*]") \
        .getOrCreate()


def test_transformar_dados(spark):
    # Definindo o schema explicitamente
    schema = StructType([
        StructField("Border", StringType(), True),
        StructField("Date", StringType(), True),
        StructField("Measure", StringType(), True),
        StructField("Value", StringType(), True),
        StructField("Port_Name", StringType(), True),
        StructField("State", StringType(), True),
        StructField("Latitude", StringType(), True),
        StructField("Longitude", StringType(), True),
        StructField("Point", StringType(), True)
    ])

    # Dados de entrada como lista de tuplas
    input_data = [
        ("US-Canada Border", "Jan 2024", "Personal Vehicle Passengers",
         "1000", "Buffalo", "NY", "42.9", "-78.9", "dummy")
    ]

    # Criando DataFrame com schema explícito
    df_input = spark.createDataFrame(input_data, schema)

    # Aplica transformação
    df_resultado = transformar_dados(df_input)

    # Testes básicos
    assert df_resultado.count() == 1

    expected_columns = {"port_name", "state", "year", "month",
                        "vehicle_category", "total_value"}
    assert expected_columns.issubset(set(df_resultado.columns))

    row = df_resultado.first()
    assert row.port_name == "Buffalo"
    assert row.state == "NY"
    assert row.year == 2024
    assert row.month == 1
    assert row.vehicle_category == "Passenger"
    assert row.total_value == 1000.0