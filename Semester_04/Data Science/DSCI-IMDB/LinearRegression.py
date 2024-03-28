import pandas as pd
import seaborn as sns
import pickle 
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
import numpy as np
pd.set_option('display.max_columns', None)

current_directory = os.getcwd()
file_path = os.path.join(current_directory,'linear.pickle')
file_path2 = os.path.join(current_directory,'linear_output.pickle')
df = pd.read_csv('imdb_top_1000.csv')
df.dropna(inplace=True)
print(df.columns)

conditions = [df['IMDB_Rating'] > 5, df['IMDB_Rating'] <= 5]
labels_rating = ['Popular', 'Unpopular']

df['Rating_Category'] = np.select(conditions, labels_rating, default='Unknown')

df['Gross'] = df['Gross'].str.replace(',', '').astype(float)
gross_stats = df['Gross'].describe()
gross_min = gross_stats['min']
gross_median = gross_stats['50%']  
gross_max = gross_stats['max']
conditions = [
    (df['Gross'] < gross_min),
    (df['Gross'] >= gross_min) & (df['Gross'] < gross_median),
    (df['Gross'] >= gross_median) & (df['Gross'] <= gross_max)
]
labels_gross = ['Low', 'Medium', 'High']

df['Gross Group'] = np.select(conditions, labels_gross, default='Unknown')

print("Minimum Gross:", gross_min)
print("Median Gross:", gross_median)
print("Maximum Gross:", gross_max)
print (df)
output = df['Rating_Category']
output , uniques = pd.factorize(output)
cat_features = df[['Genre', 'Director', 'Gross Group']]
num_features = df[['No_of_Votes','Meta_score']]

for feature in cat_features:
    print (feature)
    print (cat_features[feature].unique())
    
encoders = {}
for feature in cat_features:
    encoder = LabelEncoder()
    encoded_values = encoder.fit_transform(cat_features[feature])
    cat_features.loc[:, feature] = encoded_values
    encoders[feature] = encoder
    
for feature in cat_features:
    print (feature)
    print (cat_features[feature].unique())
num_features = pd.get_dummies(num_features)  
features = pd.concat([cat_features, num_features], axis=1)


x_train, x_test, y_train, y_test = train_test_split(features, output, test_size=0.3, random_state=42)

linear = LinearRegression()

linear.fit(x_train, y_train)

y_test_pred = linear.predict(x_test)

r2 = r2_score(y_test, y_test_pred)

print("R-squared score:", r2)

with open(file_path, 'wb') as rf_pickle:
    pickle.dump(linear, rf_pickle) 
    rf_pickle.close() 

with open(file_path2, 'wb') as output_pickle:
    pickle.dump(uniques, output_pickle) 
    output_pickle.close() 

coefficients = linear.coef_
feature_names = features.columns

coefficients_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})

coefficients_df['AbsoluteCoefficient'] = coefficients_df['Coefficient'].abs()
coefficients_df = coefficients_df.sort_values(by='AbsoluteCoefficient', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Coefficient', y='Feature', data=coefficients_df)
plt.title('Feature Coefficients in Linear Regression Model')
plt.xlabel('Coefficient')
plt.ylabel('Feature')
plt.tight_layout()
plt.savefig('Linear_feature_importance.png') 
