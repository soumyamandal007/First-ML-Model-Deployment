#we will create our ML model
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

#load the csv file
df = pd.read_csv('iris.csv')

print(df.head())

#selecting independent and dependent variables
X = df[["Sepal_Length" , "Sepal_Width", "Petal_Length", "Petal_Width"]]
y = df["Class"]

#SPlit the data set
X_train , X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

#Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Instantiate Model
classifier = RandomForestClassifier()

classifier.fit(X_train, y_train)

pickle.dump(classifier, open("model.pkl", "wb"))