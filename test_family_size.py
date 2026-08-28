from src.ingestion.spark_session import get_spark_session
from src.ingestion.load_data import load_titanic_data
from src.features.family_size import FamilySizeAdder
from src.features.is_alone import IsAloneAdder
from src.features.title import TitleExtractor


spark = get_spark_session("TestFeatures")

df = load_titanic_data(spark, "data/raw/titanic.csv")

df = FamilySizeAdder().transform(df)
df = IsAloneAdder().transform(df)
df =  TitleExtractor().transform(df)


df.select("PassengerId", "SibSp", "Parch", "FamilySize", "IsAlone", "Name", "Title").show(10)