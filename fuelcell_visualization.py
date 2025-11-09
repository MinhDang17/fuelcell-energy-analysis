import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --- Dữ liệu giả lập ---
np.random.seed(42)
N = 300
df = pd.DataFrame({
    'flight_time': np.arange(N),
    'temperature': np.random.normal(25, 5, N),
    'humidity': np.random.uniform(30, 70, N),
    'load_power': np.random.uniform(100, 600, N),
    'hydrogen_flow': np.random.uniform(0.2, 1.2, N),
})
df['efficiency'] = 80 - 0.03*(df['temperature']-25)**2 - 0.01*(df['humidity']-50)**2 + np.random.normal(0,1,N)

# --- Visualization 1: xu hướng hiệu suất ---
plt.figure(figsize=(8,4))
sns.lineplot(data=df, x='flight_time', y='efficiency', color='blue')
plt.title('Fuel Cell Efficiency Trend Over Flight Time')
plt.xlabel('Flight Time (s)')
plt.ylabel('Efficiency (%)')
plt.savefig('images/energy_trends.png', bbox_inches='tight')
plt.show()

# --- Visualization 2: heatmap tương quan ---
plt.figure(figsize=(6,5))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation between Variables')
plt.savefig('images/correlation_heatmap.png', bbox_inches='tight')
plt.show()

# --- Visualization 3: scatter hydrogen vs efficiency ---
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='hydrogen_flow', y='efficiency', hue='load_power', palette='viridis')
plt.title('Hydrogen Flow Rate vs Efficiency')
plt.savefig('images/hydrogen_usage.png', bbox_inches='tight')
plt.show()
