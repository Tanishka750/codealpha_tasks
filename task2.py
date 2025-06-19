import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv('GlobalLandTemperaturesByCity.csv')

# Convert 'dt' column to datetime
df['dt'] = pd.to_datetime(df['dt'])

# Create new column 'Year'
df['Year'] = df['dt'].dt.year

# Drop missing values
df = df.dropna(subset=['AverageTemperature'])

# Optional: Group or filter data to keep it manageable
df_sample = df[['AverageTemperature', 'AverageTemperatureUncertainty', 'Year']]

# ➕ Correlation matrix calculation
corr = df_sample.corr()

# ➕ Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Numerical Features")
plt.tight_layout()
plt.show()
