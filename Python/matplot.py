import numpy as np 
import matplotlib.pyplot as plt 

#Joint bar graph  
# X = ['CS','IT','AIDS','EXTC']
# p2019 = [10,20,20,40]
# p2020 = [20,30,25,30]
# p2021 = [45,50,25,40]

  
# X_axis = np.arange(len(X))
  
# plt.bar(X_axis, p2019, 0.4, label = '2019')
# plt.bar(X_axis + 0.2, p2020, 0.4, label = '2020')
# plt.bar(X_axis + 0.4, p2021, 0.4, label = '2021')

  
# plt.xticks(X_axis, X)
# plt.xlabel("Groups")
# plt.ylabel("Number of Students")
# plt.title("Number of Students in each group")
# plt.legend()
# plt.show()

#Scatterd graph
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# plt.scatter(x, y)

# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y)
# plt.xlabel("Number of students")
# plt.ylabel("Marks out of 150")
# plt.show()

#Bar graph
# x = np.array(["BMW", "Mercedes-Benz", "Audi", "Range Rover"])
# y = np.array([3, 8, 1, 10])
# plt.xlabel("Brands")
# plt.ylabel("Cars sold in this month")
# plt.bar(x, y, color = "blue", width=0.5)
# plt.show()


# #Pie chart
# y = np.array([35, 25, 25, 15])
# mylabels = ["IIT-B", "TSEC", "DJS", "KJS"]
# myexplode = [0.2, 0, 0, 0]
# mycolors = ["blue","red","green","orange"]

# plt.pie(y, labels = y, explode = myexplode, labeldistance=0.5, colors=mycolors)
# plt.pie(y, labels = mylabels, explode = myexplode)
# plt.legend(loc='upper left', title= 'Placement')
# plt.show() 