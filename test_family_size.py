from src.ingestion.spark_session import get_spark_session
from src.ingestion.load_data import load_titanic_data
from src.features.family_size import FamilySizeAdder


spark = get_spark_session("TestFamilySize")

df = load_titanic_data(spark, "data/raw/titanic.csv")

adder = FamilySizeAdder()
df_with_family_size = adder.transform(df)

df_with_family_size.select("PassengerId", "SibSp", "Parch", "FamilySize").show(10)