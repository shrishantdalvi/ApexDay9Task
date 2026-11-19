import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import time

#Loading dataset csv file
df = pd.read_csv("Sample - Superstore.csv",encoding="latin1")

#Displaying first and last 10records
print(df.head(10))
print(df.tail(10))

#displaying dataset information and statistics
print(df.info())
print(df.describe())

#Displaying columns and its datatypes
print(df.dtypes)

#Finding missing values and removing missing values
print("missing values:\n",df.isnull().sum())   #No missing values

#Finding dupicated rows and removing duplicated rows
print("Duplicated rows:\n",df.duplicated().sum())  #No duplicated records

#finding unique values from categorical columns
print("Segments:\n",df["Segment"].unique())
print("Country:\n",df["Country"].unique())
print("City:\n",df["City"].unique())
print("State:\n",df["State"].unique())
print("Region:\n",df["Region"].unique())
print("Category:\n",df["Category"].unique())
print("Sub-Category:\n",df["Sub-Category"].unique())

#Removing extraspaces from columns
df.columns = df.columns.str.strip()
print("After removing Extraspaces:\n",df.columns)

#checking invalid and inconsistent data
print("Invalid Sales:",df[df["Sales"] < 0].shape[0])
print("Invalid Quantity:",df[df["Quantity"] < 0].shape[0])
print("Invalid Sales:",df[(df["Discount"] < 0) | (df["Discount"] > 1)].shape[0])

# Convert Order Date
df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="%m/%d/%Y", errors="coerce"
)

# Convert Ship Date
df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], format="%m/%d/%Y", errors="coerce"
)

#displaying dates in date-month-year format 
print(df["Order Date"].dt.strftime("%d-%m-%Y").head(10))
print(df["Ship Date"].dt.strftime("%d-%m-%Y").head(10))

#verifying datatypes and missing values
print(df[["Order Date", "Ship Date"]].dtypes)

print("Missing Order Date:", df["Order Date"].isna().sum())
print("Missing Ship Date:", df["Ship Date"].isna().sum())

#checking inconsistencies
invalid_dates = df[df["Ship Date"] < df["Order Date"]]

print("Invalid Date Records:", invalid_dates.shape[0])

#Total Sales 
Total_sales = df["Sales"].sum()
print("Total Sales:- ",Total_sales)

#Total Profit
Total_profit = df["Profit"].sum()
print("Total Profit:- ",Total_profit)

#Average Sales
Avg_sales = df["Sales"].mean()
print("Average Sales:- ",Avg_sales)

#Average Profit
Avg_profit = df["Profit"].mean()
print("Average Sales:- ",Avg_profit)

#Total orders
Total_orders = df["Order ID"].nunique()
print("Total Orders:- ",Total_orders)

#Number  of Unique customers
uniqu_customers = df["Customer ID"].nunique()
print("Number of unique Customers:- ",uniqu_customers)

#Number of Products solds
product_sold = df["Quantity"].sum()
print("Total Number of Products sold:- ",product_sold)

#Best selling Product
Best_selling_product = df.groupby("Product Name")["Quantity"].max().idxmax()
print("Best Selling Product:- ",Best_selling_product)

#Heighest  revenue Category
Highest_category_sales = df.groupby("Category")["Sales"].sum()
Highest_category = Highest_category_sales.idxmax()
print("Highest revenue Category:- ",Highest_category)

#Top10 customers by sales
Top10_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("Top10 Customers by sales:- ",Top10_customers)

#top5 cities
top5_cities = df.groupby("City")["Sales"].sum().sort_values(ascending=False).head()
print("Top5 cities:- ",top5_cities)

#Display number of Order gretaer then 1000
orders = df[df["Sales"] > 1000]
count_order = orders.shape[0]
print("Number of Orders Greater then 1000:- ",count_order)

#Display/Filter data for West Region
filtr = df[df["Region"] == "West"]
count_data = filtr.shape[0]
print("Data for West Region:- ",count_data)

#Number of Products above the avg Profit 
Above_avg_profit = df[df["Profit"] > Avg_profit]
print("Profir Above the Average:- ",Above_avg_profit)

#Top Performing month
Monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
topmonth = Monthly_sales.idxmax()
print("The Top Performing Month is:- ",topmonth)

#Display Total Sales by Region
Sales_region = df.groupby("Region")["Sales"].sum()
print("Total Sales by Regions:- ",Sales_region)

#Display Total Profit by category
profit_category = df.groupby("Category")["Profit"].sum()
print("Total Profit by category:- ",profit_category)

#Montly Sales
monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
print("Monthly Sales:- ",monthly_sales)

#Customer Wise revenue
customer_revenue = df.groupby("Customer Name")["Sales"].sum()
print("Customer wise Revenue:- ",customer_revenue)

#product wise quantity sold
Product_quantity = df.groupby("Product Name")["Quantity"].sum()
print("Quantity Sold by Product:- ",Product_quantity)

#unit prices
df["Unit Price"] = df["Sales"] / (df["Quantity"] * (1-df["Discount"]))
print(df["Unit Price"])

#total sales by unit price * discount
df["Total Sales"] = df["Quantity"] * df["Unit Price"]
print(df["Total Sales"])

#Profit margin
df["Profit Margin(%)"] = (df["Profit"] / df["Sales"])*100
print(df[["Profit","Sales","Profit Margin(%)"]].head(10))

#Discount amount
df["Discount Amount"] = df["Total Sales"] - df["Sales"]
print(df[["Discount","Sales","Discount Amount"]].head(10))

#Net Sales
df["Net Sales"] = df["Total Sales"] - df["Discount Amount"]
print(df[["Total Sales","Net Sales"]].head(10))

#Order Month Oder year
df["Order Month"] = df["Order Date"].dt.month_name()
df["Order Year"] = df["Order Date"].dt.year
print(df[["Order Month","Order Year"]])

#Profit Category
df["profit Category"] = df["Profit"].apply(
    lambda x:"High" if x > 500
    else "Medium" if x >= 100
    else "Low"
)
print(df["profit Category"])

#Top10 Products by Sales
Top10_Products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print(Top10_Products)

#Region wise Sales and category
Region_wise_sales = df.groupby("Region")["Sales"].sum()
print(Region_wise_sales)
print(profit_category)

#Average Order value
AOD = df["Sales"].sum() / df["Order ID"].nunique()
print("Average Order Value: ",round(AOD,2))
#Data Visualisation

#Monthly Sales Trend
""" monthly_sales.index = monthly_sales.index.to_timestamp()
plt.figure(figsize=(8,5))
plt.plot(monthly_sales.index,monthly_sales.values,
         color ="#35B6F6",
         linewidth =2.8,
         marker = "o",
         markersize =5,
         markerfacecolor = "#20D6B0",
         markeredgecolor = "white",
         label = "Monthly Sales")
         
plt.title("Monthly Sales Trend",fontsize=16,fontweight="bold")
plt.xlabel("Months",fontsize=12,fontweight="bold")
plt.ylabel("Sales",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)


plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.grid(axis="y", color="#64748B", linestyle="--", linewidth=0.7, alpha=0.25)

plt.title("Monthly Sales Trend", color="white", fontsize=16, fontweight="bold")
plt.xlabel("Months", color="#38BDF8")
plt.ylabel("Sales", color="#38BDF8")
plt.tick_params(colors="#DCEBFA")


plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.tick_params(colors="#DCEBFA")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
"""
#Sales by Category bar chart
Sales_category = df.groupby("Category")["Sales"].sum()
plt.bar(Sales_category.index,
        Sales_category.values,
         color="#4C78A8",
         edgecolor="#3A3A3A",
         linewidth=1.2)
 
plt.title("Total Sales by Category",
          fontsize=16, fontweight="bold", color="white", pad=20)
"""
plt.xlabel("Category",fontsize=12,fontweight="bold")
plt.ylabel("Total Sales",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
 """
plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.grid(axis="y", color="#64748B", linestyle="--", linewidth=0.7, alpha=0.25)



plt.xlabel("Months", color="#38BDF8")
plt.ylabel("Sales", color="#38BDF8")
plt.tick_params(colors="#DCEBFA")
plt.grid(axis="x",visible=False)
plt.tight_layout()
plt.show()

#Top10 customers by sales
plt.figure(figsize=(12, 7))

bars = plt.barh(
    Top10_customers.index,
    Top10_customers.values,
    color="#A78BFA",
    height=0.65,
    edgecolor="white",
    linewidth=0.7
)


plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.title("TOP 10 CUSTOMERS BY SALES",
          fontsize=16, fontweight="bold", color="white", pad=20)

plt.xlabel("Total Sales (USD)", fontsize=12, color="#38BDF8",
           fontweight="bold")
plt.ylabel("Customer Name", fontsize=12, color="#38BDF8",
           fontweight="bold")


for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2,
             f"${width:,.0f}",
             va="center", ha="left",
             color="white", fontsize=9, fontweight="bold")


plt.grid(axis="x", color="#64748B",
         linestyle="--", linewidth=0.7, alpha=0.25)

plt.gca().set_axisbelow(True)
plt.gca().set_xlim(0, Top10_customers.max() * 1.18)

plt.tick_params(colors="#DCEBFA")

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_color("#3B82F6")
plt.gca().spines["bottom"].set_color("#3B82F6")

plt.tight_layout()
plt.show() 

#Region wise sales
plt.bar(Region_wise_sales.index,
        Region_wise_sales.values,
         color="#4C78A8",
         edgecolor="#3A3A3A",
         linewidth=1.2)

plt.title("Total Sales by Region",
          fontsize=16,
          fontweight="bold",
          pad=15,
          color="white")
plt.xlabel("Region",fontsize=12,fontweight="bold")
plt.ylabel("Sales",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)

plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.grid(axis="y", color="#64748B", linestyle="--", linewidth=0.7, alpha=0.25)

#plt.title("Monthly Sales Trend", color="white", fontsize=16, fontweight="bold")
plt.xlabel("Region", color="#38BDF8")
plt.ylabel("Sales", color="#38BDF8")
plt.tick_params(colors="#DCEBFA")
plt.grid(axis="x",visible=False)
plt.tight_layout()
plt.show()

#Profit by category

plt.bar(profit_category.index,
        profit_category.values,
         color="#06B6D4",
         edgecolor="#A5F3FC",
         linewidth=1.2)

plt.title("Total Profit by Category",
          fontsize=16,
          fontweight="bold",
          pad=15)
plt.xlabel("Category",fontsize=12,fontweight="bold")
plt.ylabel("Total Profit",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)

plt.gcf().set_facecolor("#080F1E")
plt.gca().set_facecolor("#14243D")

plt.grid(axis="y", color="#38BDF8", linestyle="--", linewidth=0.7, alpha=0.25)

plt.title("Profit by Category", color="#FFFFFF", fontsize=16, fontweight="bold")
plt.xlabel("Category", color="#22D3EE")
plt.ylabel("Profit", color="#22D3EE")
plt.tick_params(colors="#E0F2FE")
plt.grid(axis="x",visible=False)
plt.tight_layout()
plt.show()

#Top10 products by Sales
plt.figure(figsize=(12, 7))

bars = plt.barh(
    Top10_Products.index,
    Top10_Products.values,
    color="#A78BFA",
    height=0.65,
    edgecolor="white",
    linewidth=0.7
)


plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.title("TOP 10 Product BY SALES",
          fontsize=16, fontweight="bold", color="white", pad=20)

plt.xlabel("Total Sales (USD)", fontsize=12, color="#38BDF8",
           fontweight="bold")
plt.ylabel("Customer Name", fontsize=12, color="#38BDF8",
           fontweight="bold")


for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2,
             f"${width:,.0f}",
             va="center", ha="left",
             color="white", fontsize=9, fontweight="bold")


plt.grid(axis="x", color="#64748B",
         linestyle="--", linewidth=0.7, alpha=0.25)

plt.gca().set_axisbelow(True)
plt.gca().set_xlim(0, Top10_Products.max() * 1.18)

plt.tick_params(colors="#DCEBFA")

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_color("#3B82F6")
plt.gca().spines["bottom"].set_color("#3B82F6")

plt.tight_layout()
plt.show()

#Distribution of Sales Histogram

plt.figure(figsize=(12,7))
plt.hist(df["Sales"],
         edgecolor ="#283618",
         color="#6A994E",
         linewidth = 1.2,
        )


plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.title("Distribution Of sales by Histogram",
          fontsize = 16,
          fontweight ="bold",
          color = "#7DFFB6")

plt.xlabel("Sales",fontsize=12,fontweight="bold", color = "#35E4FF")
plt.ylabel("Frequency",fontsize=12,fontweight="bold",color="#35E4FF")
plt.tick_params(axis="both", colors="#E2E8F0", labelsize=11)
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.grid(axis="x",visible=False)
plt.tight_layout()
plt.show() 
 
#day9 tasks
#products generated highest profit
max_profit_byproducts = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)
print(max_profit_byproducts)

#mean od numeric columns
new_numeric_cols = [
    'Sales',
    'Quantity',
    'Discount',
    'Profit',
    'Unit Price',
    'Total Sales',
    'Profit Margin(%)',
    'Discount Amount',
    'Net Sales'
]
print("mean of numeric columns:- \n",df[new_numeric_cols].mean())

#Median of numeric columns
print("Median of numeric columns:- \n",df[new_numeric_cols].median())

#Mod of numeric columns
print("Mode of numeric columns:- \n",df[new_numeric_cols].mode().iloc[0])

#standard deviation
print("Standard Deviation of numeric columns:- \n",df[new_numeric_cols].std())

#variance 
print("Variance of numeric columns:- \n",df[new_numeric_cols].var())

#quartiles and interquartiles range

Q1 = df[new_numeric_cols].quantile(0.25)
Q2 = df[new_numeric_cols].quantile(0.50)
Q3 = df[new_numeric_cols].quantile(0.75)
print("\n")
print("Q1 25%: \n",Q1)
print("Q2 50%: \n",Q2)
print("Q3 75%: \n",Q3)

IQR = Q3 - Q1
print("\nThe InterQuartile range is: \n",IQR)

#Identifing outliers

lower_bound = Q1 - 1.5*IQR
upper_bound = Q2 + 1.5*IQR

outliers = {}

for col in df[new_numeric_cols]:
    outliers[col] = df[
        (df[col] < lower_bound[col]) |
        (df[col] > upper_bound[col])
    ][col]

for col in new_numeric_cols:
    print(f" \n{col} Outliers: {len(outliers[col])}")
print(df.columns)

#correlation matrix


correlation_matrix = df[new_numeric_cols].corr()
print("\n Correlation matrix:- \n",correlation_matrix)

#data visualisation 
#profit distribution by boxplot
plt.figure(figsize=(10, 6), facecolor="#0B1530")

ax = plt.gca()
ax.set_facecolor("#111F3D")

plt.boxplot(
    df["Profit"].dropna(),
    patch_artist=True,
    widths=0.4,

    boxprops=dict(
        facecolor="#00B4D8",
        edgecolor="#FFFFFF",
        linewidth=1.5
    ),

    medianprops=dict(
        color="#FFD700",
        linewidth=2.5
    ),

    whiskerprops=dict(
        color="#FFFFFF",
        linewidth=1.5
    ),

    capprops=dict(
        color="#FFFFFF",
        linewidth=1.5
    ),

    flierprops=dict(
        marker="o",
        markerfacecolor="#FF4B5C",
        markeredgecolor="#FFFFFF",
        markersize=5,
        alpha=0.8
    )
)

# Title
plt.title(
    "Profit Distribution by Box Plot",
    fontsize=17,
    fontweight="bold",
    color="#FFFFFF",
    pad=18
)

# Axis Labels
plt.xlabel("Profit", fontsize=12, color="#FFFFFF", labelpad=10)
plt.ylabel("Profit Amount", fontsize=12, color="#FFFFFF", labelpad=10)

#plt.xticks([1], ["Profit"], color="white", fontsize=11)
plt.yticks(color="white", fontsize=10)

# Grid
plt.grid(
    axis="y",
    linestyle="--",
    linewidth=0.7,
    color="#8FAADC",
    alpha=0.25
)

# Axis borders
for spine in ax.spines.values():
    spine.set_color("#8FAADC")
    spine.set_linewidth(1)

ax.tick_params(axis="both", colors="white")

plt.tight_layout()
plt.show()

#correlation of all numeric columns by Heatmap
plt.figure(figsize=(12, 8), facecolor="#0B1530")

ax = plt.gca()
ax.set_facecolor("#111F3D")

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    center=0,
    linewidths=1.5,
    linecolor="#0B1530",
    square=True,
    annot_kws={
        "size": 11,
        "weight": "bold",
        "color": "white"
    },
    cbar_kws={
        "shrink": 0.85,
        "label": "Correlation Strength"
    }
)

plt.title(
    "Correlation Heatmap",
    fontsize=19,
    fontweight="bold",
    color="white",
    pad=20
)

plt.xticks(
    rotation=35,
    ha="right",
    fontsize=10,
    color="white",
    fontweight="bold"
)

plt.yticks(
    rotation=0,
    fontsize=10,
    color="white",
    fontweight="bold"
)

# Colorbar styling
cbar = ax.collections[0].colorbar
cbar.ax.yaxis.label.set_color("white")
cbar.ax.tick_params(colors="white")
cbar.ax.yaxis.label.set_size(11)

plt.tight_layout()
plt.show()


# Create figure
plt.figure(figsize=(10, 7), facecolor="#0B1530")

# Plot area
ax = plt.gca()
ax.set_facecolor("#111F3D")

# Pie Chart
wedges, texts, autotexts = plt.pie(
    Sales_category,
    labels=Sales_category.index,
    autopct='%1.1f%%',
    startangle=140,
    explode=(0.05, 0.05, 0.05),
    shadow=True,
    colors=["#00B4D8", "#FFD166", "#FF4B5C"],
    wedgeprops=dict(edgecolor="#0B1530", linewidth=2),
    textprops=dict(color="white", fontsize=12, fontweight="bold"),
    pctdistance=0.65,
    labeldistance=1.12
)

# Percentage styling
for autotext in autotexts:
    autotext.set_color("#0B1530")
    autotext.set_fontsize(11)
    autotext.set_fontweight("bold")

# Title
plt.title(
    "Sales Distribution by Product Category",
    fontsize=17,
    fontweight="bold",
    color="white",
    pad=20
)

plt.tight_layout()
plt.show()

max_order_bycity = df.groupby("City")["Quantity"].sum().idxmax()
print("max number of orders by city:- ",max_order_bycity)

max_profit_bysegment = df.groupby("Segment")["Profit"].sum().idxmax()
print(max_profit_bysegment)