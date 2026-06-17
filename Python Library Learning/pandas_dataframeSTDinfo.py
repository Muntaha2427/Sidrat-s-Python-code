import pandas as pd
StudentInfo= {"Name" : ["Muntaha","Charlie","Aryan","Sidrat"],
              "ID" : [243427,241045,251012,243215],
              "District":["Feni","Dhaka","Sylhet","Chittagong"],
              }
data_store=pd.DataFrame(StudentInfo)
print(data_store)