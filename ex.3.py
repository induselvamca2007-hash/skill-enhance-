import pandas as pd
import numpy as np
data={
"Id":[1,2,3,4,4,5,6],
"Name":["Asha","Balan","chitra","deva","deva","Elango",None],
"Age":[21,np.nan,23,22,22,np.nan,25],
"Salary":["25000","30000","NaN","28000","28000","32000","27000"],
"City":["Chennai","Coimbatore",None,"Chennai","Chennai","Salem","Erode"]
 }
df=pd.DataFrame(data)
print("original dataset:\n",df)
print("\n missing values per column:\n",df.isnull().sum())
df["Age"].fillna(df["Age"].median(),inplace=True)
df["Name"].fillna(df["Name"].mode()[0],inplace=True)
df["City"].fillna(df["City"].mode()[0],inplace=True)
df["Salary"]=pd.to_numeric(df["Salary"],errors="coerce")
df["Salary"].fillna(df["Salary"].mean(),inplace=True)
df["Salary"]=df["Salary"].astype(int)
print("\nDuplicate rows:\n",df[df.duplicated()])
df=df.drop_duplicates()
print("\ncleaned dataset:\n",df)
print("\n data types after cleaning :\n",df.dtypes)

