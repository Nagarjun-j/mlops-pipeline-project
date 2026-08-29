from pyspark.sql.functions import col

class EmbarkedFiller:
    def transform(self, df):
        mode_row = df.groupBy("Embarked").count().orderBy(col("count").desc()).first()
        mode_value = mode_row["Embarked"]
        return df.na.fill({"Embarked": mode_value})