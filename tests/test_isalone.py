from src.ingestion.spark_session import get_spark_session
from src.features.is_alone import IsAloneAdder
from chispa.dataframe_comparer import assert_df_equality
from pyspark.sql.types import StructType, StructField, IntegerType, LongType

def test_is_alone_adder():
    spark = get_spark_session("test_is_alone_adder")

    #Arrange
    input_df = spark.createDataFrame([(1,), (2,), (3,), (4,), (1,)], ["FamilySize"])

    #Act
    result_df = IsAloneAdder().transform(input_df)

    #Assert
    expected_df = spark.createDataFrame([(1,1), (2,0), (3,0), (4,0), (1,1)], StructType([
        StructField("FamilySize", LongType(), True),
        StructField("IsAlone", IntegerType(), False)
    ]))

    assert_df_equality(result_df, expected_df)
