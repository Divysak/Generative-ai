#241 Import pandas
import pandas as pd
#242 Create series
s=pd.Series([1,2,3]); print(s)
#243 Create DataFrame
df=pd.DataFrame({"A":[1,2],"B":[3,4]}); print(df)
#244 Head
print(df.head())
#245 Info
print(df.info())

#246 Describe
print(df.describe())
#247 Select column
print(df["A"])
#248 Select multiple
print(df[["A","B"]])
#249 iloc row
print(df.iloc[0])
#250 loc row
print(df.loc[0])

#251 Add column
df["C"]=[5,6]; print(df)
#252 Drop column
print(df.drop("C", axis=1))
#253 Filtering
print(df[df["A"]>1])
#254 Sorting
print(df.sort_values(by="B"))
#255 Count null
print(df.isnull().sum())

#256 Fill missing
df2=pd.DataFrame({"x":[1,None,3]})
print(df2.fillna(0))
#257 Unique
print(df["A"].unique())
#258 Rename
print(df.rename(columns={"A":"X"}))
#259 Read CSV (just example)
#print(pd.read_csv("file.csv"))
print("skip - file not available")

#260 Shape
print(df.shape)
#261 Groupby
print(df.groupby("B").count())
#262 Add row
df.loc[2]=[5,6,7]; print(df)
#263 Drop row
print(df.drop(2))
#264 Index reset
print(df.reset_index(drop=True))

#265 Column dtype
print(df["A"].dtype)
#266 Convert dtype
df["A"]=df["A"].astype(float); print(df)
#267 Set index
print(df.set_index("B"))
#268 Unique count
print(df["A"].nunique())
#269 Value counts
print(df["B"].value_counts())
#270 Export CSV (example)
#df.to_csv("output.csv")
print("done - file not saved here")
