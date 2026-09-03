from src.ingestion.spark_session import get_spark_session
from src.features.embarked_filler import EmbarkedFiller
from chispa.dataframe_comparer import assert_df_equality
from pyspark.sql.types import StructType, StructField, StringType


def test_embarked_filler():
    spark = get_spark_session("test_embarked_filler")

    # Arrange: S appears most often, one null to be filled
    input_df = spark.createDataFrame(
        [("S",), ("S",), ("C",), (None,)],
        ["Embarked"]
    )

    # Act
    result_df = EmbarkedFiller().transform(input_df)

    # Assert
    expected_df = spark.createDataFrame(
        [("S",), ("S",), ("C",), ("S",)], StructType([
            StructField("Embarked", StringType(), False)
        ])
    )

    assert_df_equality(result_df, expected_df)