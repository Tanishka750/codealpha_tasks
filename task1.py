import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("GlobalLandTemperaturesByCity.csv")

df = df.dropna(subset=["AverageTemperature"])


df['dt'] = pd.to_datetime(df['dt'])


latest_data = df[df['dt'].dt.year == 2012]


cities = ['Delhi', 'London', 'Sydney', 'New York', 'Tokyo', 'Moscow', 'Cape Town']
city_temps = latest_data[latest_data['City'].isin(cities)]

avg_temp_by_city = city_temps.groupby('City')['AverageTemperature'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='City', y='AverageTemperature', data=avg_temp_by_city, palette='coolwarm')

for index, row in avg_temp_by_city.iterrows():
    plt.text(
        x=index,
        y=row['AverageTemperature'] + 0.4,  
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

