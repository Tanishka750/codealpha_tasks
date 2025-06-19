import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('GlobalLandTemperaturesByCity.csv')


df['dt'] = pd.to_datetime(df['dt'])


df['Year'] = df['dt'].dt.year


df = df.dropna(subset=['AverageTemperature'])


df_sample = df[['AverageTemperature', 'AverageTemperatureUncertainty', 'Year']]


corr = df_sample.corr()


plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Numerical Features")
plt.tight_layout()
plt.show()
