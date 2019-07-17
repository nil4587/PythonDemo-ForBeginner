#*************************************************************************************************#
# MACHINE LEARNING :
#*************************************************************************************************#

#-------------------------------------------------------------------------------------------------#
# A) STEPS to execute project in Machine Learning :
#-------------------------------------------------------------------------------------------------#

# 1. Import data from the .CSV file
# 2. Clean duplicate, incomplete or irrelevant data
# 3. Split the data into Training / Test sets
# 4. Create a model from the data
# 5. Train the model
# 6. Make Predictions
# 7. Evaluate and improve the prediction

#-------------------------------------------------------------------------------------------------#
# B) Libraries and Tools for Machine learning :
#-------------------------------------------------------------------------------------------------#

# 1. 'Numpy' : provides multi-dimensional array
# 2. 'Pandas' : Data analysis library, provide a concept called data-frame.
# 3. 'MatPlotLib' : 2 dimensional library for creating plotting & graphs
# 4. 'SciKit-Learn' : Provided most common algorithms for machine learning operations. (https://scikit-learn.org/stable/install.html)
# 5. 'Jupyter' : A project tool to execute the machine learning related projects. (Used just for Graphical representation)
# It provides better visualisation of output and download link : https://www.anaconda.com/download/
# 6. After downloading ANACONDA software, open the terminal, write and execute "jupyter notebook"
# which will start notebook server on mac machine to which you have installed this software and
# after that, it will open "http://localhost:8888/tree" link in browser where bydefault,
# you can see home directory of your machine
# 7. Importing a dataset using Jupyter from 'https://www.kaggle.com'
# 8. Download on of the data sets available on kaggle after login. Download "Video Game Sales" data set.
# 9. if received any error regarding PANDAS not found, use "sudo pip install pandas" command to install it
# 10. 'Jupyter notebook' command to open JUPYTER UI

#-------------------------------------------------------------------------------------------------#
# D) An example of machine learning to review the sales from a CSV file
#-------------------------------------------------------------------------------------------------#

# import pandas as pd
# df = pd.read_csv('vgsales.csv')
# print(df.shape)
# print(df.describe)  # To display the records from the .csv file
# # To get the basis statistics of the .csv file's data based on
# # Rank, Year, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales
# print(df.describe())
# print(df.values)

#-------------------------------------------------------------------------------------------------#
# E) A machine learning program to increase the sale of online music streaming application
#-------------------------------------------------------------------------------------------------#

# # Step 1 : Downloading & importing data
# # To get the accuracy of input parameters
# from sklearn.metrics import accuracy_score
# # Importing a function which splits entire data-sets in two parts : 1. Training, 2. Testing
# from sklearn.model_selection import train_test_split
# # Importing an algorithm to make predictions from user inputs
# from sklearn.tree import DecisionTreeClassifier
# import pandas as pd

# music_data = pd.read_csv('music.csv')
# print(music_data)

# # Step 2: Split main data set into multiple data sets(input & output) to make predictions work.
# # Represents a new dataset without "genre" column known as input, it won't modify the existing one
# X = music_data.drop(columns=["genre"])
# print(X)
# # Represents a dataset containing values from "genre" column
# Y = music_data["genre"]
# print(Y)

# # Step 3 : Need to create a model using an algorithm (learning & predicting)
# model = DecisionTreeClassifier()
# model.fit(X, Y)
# predictions = model.predict([[21, 1], [22, 0]])
# print(predictions)

# # Step 4 : Calculate & measure the accuracy of a model
# # Arrays with the allocation size upto 20% for testing
# X_train, X_test, Y_train, Y_test = train_test_split(
#     X, Y, test_size=0.2)  # train as input & test as output
# model.fit(X_train, Y_train)  # Input arguments for testing data sets
# # Input arguments for predictions
# predictions = model.predict(X_test)

# # Takes two arguments : 1. expected outcome, 2. Prediction inputs
# # gives the accuracy between 0 - 1.
# score = accuracy_score(Y_test, predictions)
# print(score)

#-------------------------------------------------------------------------------------------------#
# F) Persisting Models :
#-------------------------------------------------------------------------------------------------#

# # 'joblib' has methods for saving and loading models
# from sklearn.externals import joblib
# # Importing an algorithm to make predictions from user inputs
# from sklearn.tree import DecisionTreeClassifier
# import pandas as pd

# # # Step 1 : Downloading & importing data
# # music_data = pd.read_csv('music.csv')
# # print(music_data)

# # # Step 2: Split main data set into multiple data sets(input & output) to make predictions work.
# # # Represents a new dataset without "genre" column known as input, it won't modify the existing one
# # X = music_data.drop(columns=["genre"])
# # print(X)
# # # Represents a dataset containing values from "genre" column
# # Y = music_data["genre"]
# # print(Y)

# # # Step 3 : Need to create a model using an algorithm (learning & predicting)
# # model = DecisionTreeClassifier()
# # model.fit(X, Y)

# # # Step 4 : Save a model to a file,
# # joblib.dump(model, "music-recommender.joblib")

# # Step 5: load model, (you can comment out above 1-4 steps after performing all of those)
# model = joblib.load("music-recommender.joblib")

# # Step 6:
# predictions = model.predict([[21, 1]])
# print(predictions)

#-------------------------------------------------------------------------------------------------#
# G) Visualising a decision tree :
#-------------------------------------------------------------------------------------------------#

# An object has an export method for decision tree in a graphical format
from sklearn import tree
# Importing an algorithm to make predictions from user inputs
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Step 1 : Downloading & importing data
music_data = pd.read_csv('music.csv')
print(music_data)

# Step 2: Split main data set into multiple data sets(input & output) to make predictions work.
# Represents a new dataset without "genre" column known as input, it won't modify the existing one
X = music_data.drop(columns=["genre"])
print(X)
# Represents a dataset containing values from "genre" column
Y = music_data["genre"]
print(Y)

# Step 3 : Need to create a model using an algorithm (learning & predicting)
model = DecisionTreeClassifier()
model.fit(X, Y)

# '.dot' format for Graph Description Language
tree.export_graphviz(model, out_file="music-recommender.dot",
                     feature_names=['age', 'gender'],
                     class_names=sorted(Y.unique()),
                     label="all",
                     rounded=True,
                     filled=True)


# filled : To fill the box with color or not i.e True/False
# rounded : the box with rounded corner or not i.e True/False
# label : In graphical layout, every node has labels with values
# class_name: it's displayed with the unique values from 'genre' table
# feature_names : for each node has it's own title on top for condition
# TODO : To visualize the GRAPH, need to install DOT extension in Visual Code


#*************************************************************************************************#
# MIGRATION FOR CREATING TABLE with DJANGO :
#*************************************************************************************************#

# 1. First create a class with attributes prior creating a table in database
# 2. Run 'python3 manage.py makemigrations' command on terminal to migrate
# 3. After running above command a new package called 'migration' will be created under the products app
# 4. Under the 'migration' package, user can see new module called it '0001_initial.py'
# 5. After that, run 'python3 manage.py migrate' command on terminal to create the table by migrating all operations
# 6. https://getbootstrap.com : A framework to display modern and responsive application
