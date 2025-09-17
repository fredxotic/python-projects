import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import warnings
warnings.filterwarnings('ignore')

# Task 1: Load and Explore 
try:
    iris_data = load_iris()
    iris = iris_data  
    
    # Create DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    print("Dataset loaded successfully!")
    
except Exception as e:
    print(f"Error loading dataset: {e}")
    df = pd.DataFrame()

# Only proceed if df was created successfully
if not df.empty:
    print("\n First 5 rows:")
    print(df.head())
    print(f"\n Shape: {df.shape}")
    print("\n Missing values:")
    print(df.isnull().sum())

    # Task 2: Analysis
    print("\n Basic statistics:")
    print(df.describe())
    print("\n species averages:")
    print(df.groupby('species').mean())

    # Task 3: Visualization
    plt.figure(figsize=(15, 10))

    # Plot 1: Line chart
    plt.subplot(2, 2, 1)
    df_sorted = df.sort_values('sepal length (cm)')
    plt.plot(df_sorted['sepal length (cm)'], df_sorted['sepal width (cm)'], 'b-')
    plt.title('Sepal Dimensions Relationship')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.grid(True, alpha=0.3)

    # Plot 2: Bar chart - FIXED
    plt.subplot(2, 2, 2)
    means = df.groupby('species')['petal length (cm)'].mean()
    plt.bar(means.index, means.values, color=['red', 'green', 'blue']) 
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Petal Length (cm)')

    # Plot 3: Histogram
    plt.subplot(2, 2, 3)
    plt.hist(df['sepal length (cm)'], bins=15, alpha=0.7, edgecolor='black')
    plt.title('Distribution of Sepal Lengths')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)

    # Plot 4: Scatter plot
    plt.subplot(2, 2, 4)
    colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
    for species, color in colors.items():
        subset = df[df['species'] == species]
        plt.scatter(subset['sepal length (cm)'], subset['petal length (cm)'], 
                   color=color, label=species, alpha=0.7)
    plt.title('Sepal vs Petal Length by Species')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    print("\n Analysis Complete! Key findings:")
    print("- Three distinct iris species with clear measurement differences")
    print("- Setosa: Smallest flowers, Virginica: Largest flowers")
    print("- Strong correlation between sepal and petal lengths")
    print("- Data is clean and ready for machine learning models")
else:
    print("Could not proceed with analysis due to loading error")