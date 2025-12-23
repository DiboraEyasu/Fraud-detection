import pandas as pd

class GeoIntegration:
    def __init__(self, ip_df):
        self.ip_df = ip_df.copy()
        self.prepare_ip_data()


    def prepare_ip_data(self):
        """
        Convert IP range columns to integer
        """
        self.ip_df["lower_bound_ip_address"] = self.ip_df["lower_bound_ip_address"].astype(int)
        self.ip_df["upper_bound_ip_address"] = self.ip_df["upper_bound_ip_address"].astype(int)


    def map_ip_to_country(self, ip_value):
        """
        Maps single ip_address to a country
        """

        row = self.ip_df[(self.ip_df["lower_bound_ip_address"] <= ip_value) & (self.ip_df["upper_bound_ip_address"] >= ip_value)]
        return row["country"].values[0] if not row.empty else "Unknown"
    

    def add_country(self, df):
        """
        Adds the country column which was mapped to the frad databased on ip_address matching
        """

        df = df.copy()
        df["country"] = df["ip_address"].apply(lambda x: self.map_ip_to_country(x))
        return df
        