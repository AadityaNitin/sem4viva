import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# myvar = pd.DataFrame(mydataset)
# print(myvar)

#creating a series from list:
# a = [1, 7, 2]
# myvar = pd.Series(a)
# print(myvar)

#Giving custom lables to series:
# a = [1, 7, 2]
# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)

#we can also use key-value pairs to create a series 
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
# print(myvar)

# #Dataframe: DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
# print(df)

#Locating a row
# print(df.loc[0])

#We can give custom labels using index as seen above(line no:15)


#Loading files into dataframes
# df = pd.read_csv('data.csv')
# print(df.to_string()) :used to print the whole dataframe
#If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows if print(df) is used

#cleaning data
# 1)Deleting empty cells containing rows
# df = pd.read_csv('data.csv')
# new_df = df.dropna()
# print(new_df.to_string())

# 2) Replacing using mean, median, mode
# df = pd.read_csv('data.csv')
# x = df["Calories"].mean()
#or
# x = df["Calories"].median()
#or
# x = df["Calories"].mode()[0]
# df["Calories"].fillna(x, inplace = True)


#Convert into correct date format:
# df = pd.read_csv('data.csv')
# df['Date'] = pd.to_datetime(df['Date'])
# print(df.to_string())

#Removing duplicates
# df.drop_duplicates(inplace = True)