import pandas as pd
StudentInfo= {"Name" : ["Muntaha","Charlie","Aryan","Sidrat"],
              "ID" : [243427,241045,251012,243215],
              "District":["Feni","Dhaka","Sylhet","Chittagong"],
              "CGPA":[3.96,3.88,3.92,3.94]
              }
dStIf=pd.DataFrame(StudentInfo)
print(dStIf[["Name","CGPA"]])