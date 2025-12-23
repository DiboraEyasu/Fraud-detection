import pandas as pd

class FeatureEngineering:
    def __init__(self, df):
        self.df = df.copy()


    def add_time_features(self):
        self.df["time_since_signup"] = (self.df["purchase_time"] - self.df["signup_time"]).dt.total_seconds()
        self.df["hour_of_day"] = self.df["purchase_time"].dt.hour
        self.df["day_of_week"] = self.df["purchase_time"].dt.dayofweek
        return self.df
    

    def add_transaction_frequency(self):
        txn_count = self.df.groupby("user_id")["purchase_time"].count()
        self.df["txn_per_user"] = self.df["user_id"].map(txn_count)
        return self.df

