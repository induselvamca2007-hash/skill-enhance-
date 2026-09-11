import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
dates = pd.date_range("2025-01-01", periods=90, freq="D")
values = 50 + np.cumsum(np.random.randn(90))

values[30]+=25
values[60]-=20
df = pd.DataFrame({"value": values}, index=dates)

df["rolling_mean"]= df["value"].rolling(window=7).mean()
df["rolling_std"]= df["value"].rolling(window=7).std()

df["upper"] = df["rolling_mean"] + 2 * df["rolling_std"]
df["lower"] = df["rolling_mean"] - 2 * df["rolling_std"]
df["anomaly"] = (df["value"]> df["upper"]) | (df["value"] < df["lower"])

print("Detected anomalies:\n", df[df["anomaly"]])

plt.figure(figsize=(12, 6))
plt.plot(df.index, df["value"], label="Original", color="steelblue")
plt.plot(df.index, df["rolling_mean"], label="7-day Rolling Mean", color="orange")
plt.fill_between(df.index, df["lower"],df["upper"], color="orange", alpha=0.2, label="+-2 Std Band")
plt.scatter(df.index[df["anomaly"]], df["value"][df["anomaly"]], color="red",label="Anomaly", zorder=5)
plt.legend()
plt.title("Rolling Mean, Std Deviation and Anomaly Detection")
plt.savefig("rolling_anomaly.png", dpi=150)
plt.show()