class FeaturePipeline:
    def __init__(self, transformers):
        self.transformers = transformers


    def run(self, df):
        for transformer in self.transformers:
            df = transformer.transform(df)
        return df