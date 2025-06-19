import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("GlobalLandTemperaturesByCity.csv")

# Drop rows with missing values
df = df.dropna(subset=["AverageTemperature"])

# Convert 'dt' column to datetime
df['dt'] = pd.to_datetime(df['dt'])

# Filter for a recent year (e.g., 2012)
latest_data = df[df['dt'].dt.year == 2012]

# Choose some cities (you can customize this list)
cities = ['Delhi', 'London', 'Sydney', 'New York', 'Tokyo', 'Moscow', 'Cape Town']
city_temps = latest_data[latest_data['City'].isin(cities)]

# Get the average temperature for each city in 2012
avg_temp_by_city = city_temps.groupby('City')['AverageTemperature'].mean().reset_index()

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='City', y='AverageTemperature', data=avg_temp_by_city, palette='coolwarm')

for index, row in avg_temp_by_city.iterrows():
    plt.text(
        x=index,
        y=row['AverageTemperature'] + 0.4,  # little offset above bar
        s=f"{row['AverageTemperature']:.1f}°C",
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

plt.title("Average Temperature in Major Cities ")
plt.ylabel("Temperature (°C)")
plt.xlabel("City")
plt.tight_layout()
plt.show()

pivot = df.pivot_table(index='City', columns='Month', values='AverageTemperature', aggfunc='mean')
sns.heatmap(pivot, cmap='coolwarm', annot=True, fmt='.1f')

