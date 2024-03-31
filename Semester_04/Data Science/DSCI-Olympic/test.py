import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pickle 
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report 
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv(r'Semester_04\Data Science\DSCI-Olympic\dataset_olympics.csv')
# data cleaning and preparation
data['Height'].fillna(data['Height'].mean(), inplace =True)
data['Weight'].fillna(data['Weight'].mean(), inplace =True)
data.dropna(subset=['Age'], inplace = True)
data.drop_duplicates(inplace = True)
data['Medal'].replace(['Gold', 'Silver', 'Bronze'], 'Yes', inplace=True)
data['Medal'].fillna('No', inplace= True)


num_features = data[['Age','Height','Weight']]
cat_features = data[['Sex','Sport']]
output = data['Medal']

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

decision_tree_model = SVC()

decision_tree_model.fit(x_train, y_train)

y_train_pred = decision_tree_model.predict(x_train)
y_test_pred = decision_tree_model.predict(x_test)

train_accuracy = accuracy_score(y_train_pred, y_train)
test_accuracy = accuracy_score(y_test_pred, y_test)
print("Classification Report for Training Data:")
print(classification_report(y_train, y_train_pred))

print("Classification Report for Testing Data:")
print(classification_report(y_test, y_test_pred))

print("Training Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)

# fig, ax = plt.subplots() 
# ax = sns.barplot(x=decision_tree_model.feature_importances_, y=features.columns) 
# plt.title('Important Features that could predict user subcription') 
# plt.xlabel('Importance') 
# plt.ylabel('Feature') 
# plt.tight_layout() 

# fig.savefig('dtc_feature_importance.png') 