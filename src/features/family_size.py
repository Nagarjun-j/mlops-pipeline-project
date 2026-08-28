from pyspark.sql.functions import col


class FamilySizeAdder:
    def transform(self, df):
        return df.withColumn("FamilySize", col("sibSp") + col("Parch") + 1)