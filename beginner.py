# A. Matplotlib
#
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df_100 = pd.read_excel("F:\ShadowFox\Level = 1\Online_Shopping.xlsx")


# 1. Line Plot: Total Price by Order Date (Sorted)
df_line = df_100.sort_values("Order Date")
plt.figure()
plt.plot(df_line["Order Date"], df_line["Total Price"], marker='o', linestyle='-')
plt.title("Total Price by Order Date")
plt.xlabel("Order Date")
plt.ylabel("Total Price")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()  


# 2. Scatter Plot: Quantity vs Total Price
plt.figure()
plt.scatter(df_100["Quantity"], df_100["Total Price"], c='red', edgecolors='k')
plt.title("Quantity vs Total Price")
plt.xlabel("Quantity")
plt.ylabel("Total Price")
plt.grid(True)
plt.tight_layout()

plt.show() 



# 3. Bar Chart: Count of Orders by Category
category_counts = df_100["Category"].value_counts()

plt.figure()
category_counts.plot(kind='bar', color='pink', edgecolor='black')
plt.title("Number of Orders by Category")
plt.xlabel("Category")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()  # Show the bar chart


# 4. Pie Chart: Orders by Payment Method
payment_counts = df_100["Payment Method"].value_counts()

plt.figure()
payment_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, shadow=True)
plt.title("Orders by Payment Method")
plt.ylabel("")  # Hide y-label for a cleaner pie
plt.tight_layout()

plt.show()

# 5. Histogram: Distribution of Total Prices
plt.figure()
plt.hist(df_100["Total Price"], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram of Total Prices")
plt.xlabel("Total Price")
plt.ylabel("Frequency")
plt.tight_layout()

plt.show()

# B. Seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df_100 = pd.read_excel("F:\\ShadowFox\\Level = 1\\Online_Shopping.xlsx")

sns.set(style="whitegrid")

# 1. Line Plot: Total Price by Order Date
df_line = df_100.sort_values("Order Date")
plt.figure(figsize=(10, 6))
sns.lineplot(x="Order Date", y="Total Price", data=df_line, marker="o")
plt.title("Total Price by Order Date")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Scatter Plot: Quantity vs Total Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Quantity", y="Total Price", data=df_100, color="red", edgecolor='k')
plt.title("Quantity vs Total Price")
plt.tight_layout()
plt.show()

# 3. Bar Chart: Count of Orders by Category
plt.figure(figsize=(10, 6))
sns.countplot(x="Category", data=df_100, palette="pastel", edgecolor="black")
plt.title("Number of Orders by Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Pie Chart: Orders by Payment Method (using Matplotlib)
payment_counts = df_100["Payment Method"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=140, shadow=True)
plt.title("Orders by Payment Method")
plt.tight_layout()
plt.show()

# 5. Histogram: Distribution of Total Prices
plt.figure(figsize=(10, 6))
sns.histplot(df_100["Total Price"], bins=10, kde=True, color='skyblue')
plt.title("Histogram of Total Prices")
plt.tight_layout()
plt.show()

