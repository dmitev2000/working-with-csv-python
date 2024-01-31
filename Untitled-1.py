import pandas as pd
import numpy as np

# Load the datasets
circuit_data = pd.read_csv('./curcuit.csv')
census_data = pd.read_csv('./census.csv')
image_data = pd.read_csv('./image.csv')
music_data = pd.read_csv('./music.csv')

# Create a dictionary to store the results
analysis_results = {}

# Function to perform descriptive analysis
def descriptive_analysis(data, name):
    analysis = {
        'Maximum': data.max(),
        'Minimum': data.min(),
        'Mean': data.mean(),
        'Standard Deviation': data.std(),
        'Kurtosis': data.kurtosis(),
        'Skewness': data.skew()
    }
    analysis_results[name] = analysis

# Perform descriptive analysis for each dataset
descriptive_analysis(circuit_data, 'circuit.csv')
descriptive_analysis(census_data, 'census.csv')
descriptive_analysis(image_data, 'image.csv')
descriptive_analysis(music_data, 'music.csv')

# Display the results
for dataset, results in analysis_results.items():
    print(f"\nDescriptive Analysis for {dataset}:")
    for stat, value in results.items():
        print(f"{stat}: {value}")
