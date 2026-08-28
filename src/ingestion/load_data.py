from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType, StringType
from pyspark.sql import SparkSession
from src.ingestion.spark_session import get_spark_session


titanic_schema = StructType([
    StructField("PassengerId", IntegerType(), False),
    StructField("Survived", IntegerType(), True),
    StructField("Pclass", IntegerType(), True),
    StructField("Name", StringType(), False),
    StructField("Sex", StringType(), False),
    StructField("Age", DoubleType(), True),
    StructField("SibSp", IntegerType(), True),
    StructField("Parch", IntegerType(), True),
    StructField("Ticket", StringType(), False),
    StructField("Fare", DoubleType(), True),
    StructField("Cabin", StringType(), True),
    StructField("Embarked", StringType(), True),

])



def load_titanic_data(spark: SparkSession, file_path: str):
    df = spark.read.format("csv").option("header", "true").schema(titanic_schema).load(file_path)
    return df

if __name__ == "__main__":
    spark = get_spark_session()
    df = load_titanic_data(spark,"data/raw/titanic.csv")

    print("Row_count: ", df.count())
    df.show(5)