
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Dataset
df = pd.read_csv("F:\ShadowFox\Level = 2\delhiaqi.csv")
df['date'] = pd.to_datetime(df['date'])

# 1: Add Month and Season Columns
df['month'] = df['date'].dt.month

def assign_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Summer'
    elif month in [6, 7, 8]:
        return 'Monsoon'
    else:
        return 'Post-Monsoon'

df['season'] = df['month'].apply(assign_season)

# 2: Define Key Pollutants
pollutants = ['pm2_5', 'pm10', 'co', 'no', 'no2', 'o3', 'so2', 'nh3']

# 3: Handle Missing Values
df[pollutants] = df[pollutants].fillna(method='ffill')

# 4: Monthly Average Trends (Different colors)
monthly_avg = df.set_index('date').resample('MS')[pollutants].mean()
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77']

plt.figure(figsize=(15, 8))
for i, pollutant in enumerate(pollutants):
    plt.plot(monthly_avg.index, monthly_avg[pollutant], label=pollutant, color=colors[i])

plt.title('Monthly Average Concentrations of Pollutants in Delhi')
plt.xlabel('Month')
plt.ylabel('Concentration')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 5: Seasonal Boxplots with custom palette
season_palette = {'Winter': 'green', 'Summer': '#E69F00', 'Monsoon': 'green', 'Post-Monsoon': 'red'}

plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='season', y='pm2_5', order=['Winter', 'Summer', 'Monsoon', 'Post-Monsoon'], palette=season_palette)
plt.title('Seasonal Variation of PM2.5')
plt.ylabel('PM2.5 (μg/m³)')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='season', y='pm10', order=['Winter', 'Summer', 'Monsoon', 'Post-Monsoon'], palette=season_palette)
plt.title('Seasonal Variation of PM10')
plt.ylabel('PM10 (μg/m³)')
plt.grid(True)
plt.show()

# 6: Correlation Heatmap with vibrant color
plt.figure(figsize=(10, 8))
corr = df[pollutants].corr()
sns.heatmap(corr, annot=True, cmap='Spectral', fmt='.2f', linewidths=0.5)
plt.title('Correlation Between Different Pollutants')
plt.tight_layout()
plt.show()

# 7: Daily PM2.5 Trend with AQI Threshold Lines
daily_avg = df.set_index('date')['pm2_5'].resample('D').mean()

plt.figure(figsize=(14, 6))
plt.plot(daily_avg.index, daily_avg, label='Daily PM2.5', color='#6A1B9A')
plt.axhline(60, color='#2E7D32', linestyle='--', label='Moderate AQI Threshold')
plt.axhline(100, color='#F9A825', linestyle='--', label='Poor AQI Threshold')
plt.title('Daily PM2.5 Concentration in Delhi (AQI Indicator)')
plt.xlabel('Date')
plt.ylabel('PM2.5 (μg/m³)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


print("Summary Statistics of Key Pollutants:\n")
print(df[pollutants].describe())
