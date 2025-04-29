
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv(r'F:\ShadowFox\Level = 3\mock_sales_data.csv')  


print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.nunique())

df.columns = df.columns.str.strip()
df = df.dropna()


df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')


plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Revenue', color='red')  # Red line
plt.title('Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.grid(True)
plt.show()


plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='Cost', y='Profit', color='red')  # Red points
plt.title('Profit vs Cost')
plt.xlabel('Cost')
plt.ylabel('Profit')
plt.grid(True)
plt.show()
