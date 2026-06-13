import matplotlib.pyplot as plt
"""x=[1,2,3,4,5]
y=[10,20,30,40,42]
plt.plot(x,y)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple Line Graph")
plt.show()"""

subjects=["Math","Physics","ICT"]
marks=[100,85,50]
plt.bar(subjects,marks)
plt.title("Student Marks")
plt.show()