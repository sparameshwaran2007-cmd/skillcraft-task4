"""Task 04 – Marketing Campaign EDA | SkillCraft Technology
Place marketing_campaign.csv beside this script.
Run: python Task_04_Marketing_Campaign_EDA.py
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("marketing_campaign.csv", sep="\\t")
df.columns = df.columns.str.replace("\\ufeff", "", regex=False).str.strip()
df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], errors="coerce")
df["Income_Missing_Flag"] = df["Income"].isna().astype(int)
df["Income"] = df["Income"].fillna(df["Income"].median())
df = df.drop_duplicates(subset=["ID"]).copy()

products = ["MntWines","MntFruits","MntMeatProducts",
            "MntFishProducts","MntSweetProducts","MntGoldProds"]
channels = ["NumWebPurchases","NumCatalogPurchases","NumStorePurchases"]
df["Total_Spend"] = df[products].sum(axis=1)
df["Total_Purchases"] = df[channels].sum(axis=1)
df["Campaigns_Accepted"] = df[["AcceptedCmp1","AcceptedCmp2",
                              "AcceptedCmp3","AcceptedCmp4","AcceptedCmp5"]].sum(axis=1)

print("Customers:", len(df))
print("Response rate:", round(df["Response"].mean()*100, 2), "%")
print("Average spend:", round(df["Total_Spend"].mean(), 2))
print("\\nSpend by product category:\\n", df[products].sum().sort_values(ascending=False))
print("\\nPurchases by channel:\\n", df[channels].sum().sort_values(ascending=False))

df.to_csv("Task_04_Cleaned_Marketing_Campaign.csv", index=False)

df[products].sum().sort_values().plot(kind="barh", title="Spend by Product Category")
plt.tight_layout(); plt.savefig("Task_04_Product_Spend.png", dpi=160); plt.show()
df[channels].sum().sort_values().plot(kind="barh", title="Purchases by Shopping Channel")
plt.tight_layout(); plt.savefig("Task_04_Channel_Purchases.png", dpi=160); plt.show()
