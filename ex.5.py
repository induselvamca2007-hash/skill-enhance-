import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("data.csv")


print("Dataset:")
print(df.head())


correlation_matrix = df.corr()


print("\nCorrelation Matrix:")
print(correlation_matrix)


plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix,
            annot=True,
            cmap="coolwarm",
            fmt=".2f",
            linewidths=0.5)

plt.title("Correlation Matrix Heatmap")
plt.show()

threshold = 0.7

print("\nHighly Correlated Variable Pairs (|r| > 0.7):")
for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        corr_value = correlation_matrix.iloc[i, j]
        if abs(corr_value) > threshold:
            print(f"{correlation_matrix.columns[i]} "
                  f"<--> {correlation_matrix.columns[j]} "
                  f"= {corr_value:.2f}")