from pyspark.sql.functions import col, when


class IsAloneAdder:
    def transform(self, df):
        return df.withColumn("IsAlone", when(col("FamilySize") == 1, 1).otherwise(0))