from src.ingestion.spark_session import get_spark_session
from src.features.title import TitleExtractor
from chispa.dataframe_comparer import assert_df_equality

def test_title_extractor():
    spark = get_spark_session("test_title_extractor")

    # Arrange
    input_df = spark.createDataFrame(
        [
            ("Braund, Mr. Owen Harris",),
            ("Cumings, Mrs. John Bradley",),
            ("Heikkinen, Miss. Laina",),
        ],
        ["Name"]
    )

    # Act
    result_df = TitleExtractor().transform(input_df)

    # Assert
    expected_df = spark.createDataFrame(
        [
            ("Braund, Mr. Owen Harris", "Mr"),
            ("Cumings, Mrs. John Bradley", "Mrs"),
            ("Heikkinen, Miss. Laina", "Miss"),
        ],
        ["Name", "Title"]
    )

    assert_df_equality(result_df, expected_df)