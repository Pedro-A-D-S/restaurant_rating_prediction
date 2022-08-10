# imports
import pandas as pd
import numpy as np
import sklearn
import pickle
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split

# warnings
import warnings
warnings.filterwarnings('ignore')

# get data
df = pd.read_csv('flask_app\Zomato_df.csv')

# drop column
df.drop('Unnamed: 0', axis = 1, inplace = True)

# splitting data
x = df.drop('rate', axis = 1)
y = df['rate']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 10)

# Extra Trees Regression
ET_model = ExtraTreesRegressor()
ET_model.fit(x_train, y_train)

# predicted values
y_predict = ET_model.predict(x_test)

pickle.dump(ET_model, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))
print(y_predict)