import pandas as pd
data={"Student's Name": [ "Sidrat","Moon","Aryan","Shreya","Ishan","Rita","Sonu"],
      "Marks": [97,94,89,70,95,79,67]}
dataFrame=pd.DataFrame(data)
avg_marks=dataFrame['Marks'].mean() #average marks
highest_marks=dataFrame['Marks'].max() #average marks
print("Student Info:\n",dataFrame)
print("Average Marks :\n",avg_marks)
print("Highest Marks:\n",highest_marks)
print("Those who scored above 80 :\n")
print(dataFrame[dataFrame["Marks"]>80])