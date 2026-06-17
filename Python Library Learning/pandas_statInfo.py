import pandas as pd
data={"Student's Name": [ "Sidrat","Moon","Aryan","Shreya"],
      "Math": [97,94,89,70],
      "Physics":[84,91,99,88],
      "ICT":[100,93,97,90]}
dataFrame=pd.DataFrame(data)
print("Student Info:\n",dataFrame)
print("Marks Statistics Table:")
print(dataFrame.describe())
