import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the datasets
circuit_data = pd.read_csv('./curcuit.csv')
census_data = pd.read_csv('./census.csv')
image_data = pd.read_csv('./image.csv')
music_data = pd.read_csv('./music.csv')

# Create a figure and axis for subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Function to compare datasets graphically
def compare_graphically(ax, data, title):
    ax.hist(data, bins=20, alpha=0.5, label='circuit.csv', color='blue')
    ax.hist(census_data, bins=20, alpha=0.5, label='census.csv', color='green')
    ax.hist(image_data, bins=20, alpha=0.5, label='image.csv', color='orange')
    ax.hist(music_data, bins=20, alpha=0.5, label='music.csv', color='red')
    ax.set_title(title)
    ax.legend()

# Compare datasets graphically
compare_graphically(axs[0, 0], circuit_data, 'Histogram Comparison for circuit.csv')
compare_graphically(axs[0, 1], census_data, 'Histogram Comparison for census.csv')
compare_graphically(axs[1, 0], image_data, 'Histogram Comparison for image.csv')
compare_graphically(axs[1, 1], music_data, 'Histogram Comparison for music.csv')

# Calculate deviation from other datasets
deviation_census = np.abs(circuit_data - census_data).mean()
deviation_image = np.abs(circuit_data - image_data).mean()
deviation_music = np.abs(circuit_data - music_data).mean()

# Print deviation values
print(f"\nDeviation from census.csv: {deviation_census}")
print(f"Deviation from image.csv: {deviation_image}")
print(f"Deviation from music.csv: {deviation_music}")

# Show plots
plt.tight_layout()
plt.show()
