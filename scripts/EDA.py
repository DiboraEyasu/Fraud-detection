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
        Visualize the relationship using Bar and Box plots.
        Args:
            x_col (str): Categorical column (e.g., 'is_fraud')
            y_col (str): Numerical column (e.g., 'amount')
        """
        if x_col in self.data.columns and y_col in self.data.columns:
            # Set up a figure with two side-by-side plots
            fig, axes = plt.subplots(1, 2, figsize=(16, 6))

            # 1. Bar Plot (Shows the average/mean)
            sns.barplot(ax=axes[0], x=self.data[x_col], y=self.data[y_col], palette='magma')
            axes[0].set_title(f"Average {y_col} by {x_col}")

            # 2. Box Plot (Shows outliers and distribution)
            sns.boxplot(ax=axes[1], x=self.data[x_col], y=self.data[y_col], palette='viridis')
            axes[1].set_title(f"Distribution & Outliers of {y_col} by {x_col}")

            # Aesthetics
            plt.tight_layout()
            
            # SAVE the plot BEFORE calling plt.show()
            plt.savefig(f"images/{x_col}_vs_{y_col}_analysis.png")
            plt.show()
        else:
            print(f"Error: Either {x_col} or {y_col} was not found in the data.")

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
        print("Converted the datatype of the specified columns successfully")

    
