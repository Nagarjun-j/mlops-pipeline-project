from src.ingestion.spark_session import get_spark_session
from src.features.family_size import FamilySizeAdder
from chispa.dataframe_comparer import assert_df_equality



def test_family_size_adder():
    spark = get_spark_session("test_family_size")


    #Arrange: small fake input wiuth known sibsp/parch values.
    input_df =  spark.createDataFrame(
        [(1,2), (0,0), (3,1)], ["SibSp", "Parch"]
    )


    #Act: run the actual transsformer
    result_df = FamilySizeAdder().transform(input_df)

    #Assert: build the dataframe we expect and compare.
    expected_df = spark.createDataFrame([(1,2,4), (0,0,1), (3,1,5)], ["SibSp", "Parch", "FamilySize"])

    assert_df_equality(result_df, expected_df)