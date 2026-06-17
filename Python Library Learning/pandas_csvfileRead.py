import pandas as pd
data={"University" : ["CU","CUET","IIUC","RU","RUET","USTC","DIU"],
      "Established": [1966,1968,1995,1954,2003,1992,2002],
      "Ranking":[5,2,1,4,3,7,6]
      }
df=pd.DataFrame(data)
df.to_csv("Uni_Ranking.csv",index=False)
new_df=pd.read_csv("Uni_Ranking.csv")
print(new_df.head(5))

new1=pd.read_csv("Uni_Ranking1.csv")
print(new1)
