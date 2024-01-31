import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read datasets
curcuit = pd.read_csv("./curcuit.csv")
census = pd.read_csv("./census.csv")
image = pd.read_csv("./image.csv")
music = pd.read_csv("./music.csv")

# Check the column names in each DataFrame
print("Column names in curcuit:", curcuit.columns)
print("Column names in census:", census.columns)
print("Column names in image:", image.columns)
print("Column names in music:", music.columns)

# Replace 'Data' and 'image' with the correct column names in the following code

# Create a boxplot
plt.boxplot([curcuit['Data'], census['Data'], image['image'], music['music']], labels=["curcuit", "census", "image", "music"])
plt.title("192007")
plt.show()

# Calculate standard deviations
sd_curcuit = np.std(curcuit['Data'])
sd_census = np.std(census['Data'])
sd_image = np.std(image['image'])
sd_music = np.std(music['music'])

# Print standard deviations
print(f"Standard Deviation for curcuit: {sd_curcuit}")
print(f"Standard Deviation for census: {sd_census}")
print(f"Standard Deviation for image: {sd_image}")
print(f"Standard Deviation for music: {sd_music}")
