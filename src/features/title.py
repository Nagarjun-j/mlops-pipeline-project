from pyspark.sql.functions import regexp_extract, col

class TitleExtractor:
    def transform(self, df):
        return df.withColumn("Title", regexp_extract(col("Name"), r"([A-Za-z]+)\.", 1))