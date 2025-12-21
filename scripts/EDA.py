import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class EDAAnalyzer:
    """
    A class for performing exploratory data analysis
    """

    def __init__(self,  filepath):
        self.filepath = filepath
        self.data = self.load_data()


    def load_data(self):
        """
        Loads data from a specified filepath
        
        Returns a data frame
        """

        print("🔍🔍 Loading data...")
        try:
            self.data = pd.read_csv(self.filepath)
            print("✅✅ Data loaded successfully.")
            return self.data
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame() 
        
    
    def inspect_data(self):
        """
        Display basic information and statistics about the dataset.
        """
        print("Data Info:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nDuplicated Values:")
        print(self.data.duplicated().sum())
        
        print("\nFirst Few Rows:")
        print(self.data.head())

    
    def visualize_distribution(self, key_columns):
        """
        Visualize the distribution of specified columns using histograms.
        Args:
            columns (list): List of column names to visualize.
        """
        for col in key_columns:
            if col in self.data.columns:
                plt.figure(figsize=(8, 6))
                sns.histplot(self.data[col], kde=True, bins=30, color='pink')
                plt.title(f"Distribution of {col}")
                plt.xlabel(col)
                plt.ylabel("Frequency")
                plt.grid(axis='y', linestyle='--', alpha=1)
                plt.show()
                plt.savefig(f"images/{col}_distribution.png")
            else:
                print(f"Column {col} not found in the dataset.")


    def visualize_relationship(self, x_col, y_col):
        """
        Visualize the relationship between two columns using a scatter plot.
        Args:
            x_col (str): Column for the x-axis.
            y_col (str): Column for the y-axis.
        """
        if x_col in self.data.columns and y_col in self.data.columns:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=self.data[x_col], y=self.data[y_col], alpha=0.7, color='purple')
            plt.title(f"{x_col} vs. {y_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.show()
            plt.savefig(f"images/{x_col}_vs_{y_col}.png")
        else:
            print("One or more columns not found in the dataset.")


    def handle_missing_values(self):
        """
        Handle missing values in the dataset.
        """
        # Check for missing values
        print(f"Missing values before cleaning:\n{self.df.isnull().sum()}")
        
        # Fill missing values with appropriate methods
        for column in self.df.columns:
            if self.df[column].dtype == 'object':
                self.df[column] = self.df[column].fillna('Unknown')
            elif self.df[column].dtype == 'float64' or self.df[column].dtype == 'int64':
                self.df[column] = self.df[column].fillna(self.df[column].median())
        
        print(f"Missing values after cleaning:\n{self.df.isnull().sum()}")


    def dtype_converter(self):
        self.data['purchase_time'] = pd.to_datetime(self.data['purchase_time'])
        self.data['signup_time'] = pd.to_datetime(self.data['signup_time'])

    
