import pandas as pd
data = {
    "cl": [1, 2, 3, 4, 5, 6, 7, 8],
    "amt": ["45000", "38000", "52000", "61000", "29000", "73000", "48000", "55000"],
    "yrs": [23, 45, 31, 60, 19, 52, 27, 38]
}
df = pd.dataframe(data)
print("original data:\n", df)
print("\noriginal dtypes:\n", df.dtypes)
df.df.rename(columns={"c1": "custumerID", "amt": "income", "yrs": "age"})
df["income"] = df["income"].astype(float)
df["Age_Group_Equalwidth"] = pd.cut(
    df["Age"], bins=3, labels=["Young", "Middle-aged", "senior"]
)
df["income_Group_equalfreq"] = pd.qcut(
    df["income"], q=3, label=["low", "medium", "high"]
)
print("\nTransformed Dataset:\n".df)
print("\nupdataed dtypes :\n,df.dtypes")
