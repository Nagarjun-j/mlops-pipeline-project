from src.ingestion.spark_session import get_spark_session
from src.features.pipeline import FeaturePipeline
from src.features.family_size import FamilySizeAdder
from src.features.is_alone import IsAloneAdder
from src.features.title import TitleExtractor
from src.features.embarked_filler import EmbarkedFiller
from chispa.dataframe_comparer import assert_df_equality
from pyspark.sql.types import StructType, StructField, StringType, LongType, IntegerType

def test_feature_pipeline():
    spark = get_spark_session("test_feature_pipeline")

    # Arrange
    input_df = spark.createDataFrame(
        [
            ("Braund, Mr. Owen Harris", 1, 0, "S"),
            ("Heikkinen, Miss. Laina", 0, 0, None),
        ],
        ["Name", "SibSp", "Parch", "Embarked"]
    )

    # Act
    result_df = FeaturePipeline(
        [FamilySizeAdder(), IsAloneAdder(), TitleExtractor(), EmbarkedFiller()]
    ).run(input_df)

    # Assert
    expected_df = spark.createDataFrame(
        [
            ("Braund, Mr. Owen Harris", 1, 0, "S", 2, 0, "Mr"),
            ("Heikkinen, Miss. Laina", 0, 0, "S", 1, 1, "Miss"),
        ],
        StructType([
            StructField("Name", StringType(), True),
            StructField("SibSp", LongType(), True),
            StructField("Parch", LongType(), True),
            StructField("Embarked", StringType(), False),
            StructField("FamilySize", LongType(), True),
            StructField("IsAlone", IntegerType(), False),
            StructField("Title", StringType(), True),
        ])
    )

    assert_df_equality(result_df, expected_df)